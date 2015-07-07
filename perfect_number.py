# This is not deterministic. See cases below where ValueError is being raised.
def isPerfect(num):
    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen
    import re

    OPN_EXP_LIMIT = 1500  # Odd numbers > 10 ** OPN_EXP_LIMIT are probably False but unproven.
    EPN_EXP_LIMIT = 32582657  # Even numbers > 2 ** EPN_EXP_LIMIT are probably False but unproven.
    MERSENNE_LIST_URL = 'http://www.mersenne.org/primes/'
    SMALL_MERSENNE_EXPS = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]

    # This is flat-out impossible by definition
    if num <= 0:
        return False

    # All odd numbers less than 10 ** 1500 are proven False, greater numbers need to be tested
    # based on http://www.lirmm.fr/~ochem/opn/opn.pdf
    if num % 2 == 1:
        numDigits = len(str(num))
        if numDigits <= OPN_EXP_LIMIT:  # math.log10 won't work here!
            return False
        fmt = 'OPN unproven but most likely False for N > 10**{0}'
        raise ValueError(fmt.format(OPN_EXP_LIMIT))

    # All remaining (even) numbers must derive from Mersenne primes. In order to be capable of
    # doing so, there must be some integer N >= 1 where num = 2**N * (2**(N+1)-1). See also:
    # http://www.mersenne.org/primes/
    factorBits = num.bit_length() / 2
    pValStr = '1' * (factorBits + 1) + '0' * factorBits
    pVal = int(pValStr, 2)
    if num != pVal:
        return False

    # Make sure web service calls won't happen when num can fit in 256 bits or less.
    if (factorBits + 1) <= SMALL_MERSENNE_EXPS[-1]:
        if (factorBits + 1) in SMALL_MERSENNE_EXPS:
            return True
        return False

    # Finally, return True if P is in the known Mersenne prime exponents list; otherwise
    # consider EPN to be unproven and raise ValueError.
    req = urlopen(MERSENNE_LIST_URL)
    data = req.read()
    req.close()
    mersExpStrs = re.findall('(?i)m([0-9]+).txt', data)
    mersExpList = [int(expStr) for expStr in mersExpStrs]
    if (factorBits + 1) <= mersExpList[-1]:
        if (factorBits + 1) in mersExpList:
            return True
        if (factorBits + 1) <= EPN_EXP_LIMIT:
            return False
    fmt = 'EPN unproven but most likely False for N > 2**{0}'
    raise ValueError(fmt.format(EPN_EXP_LIMIT))
