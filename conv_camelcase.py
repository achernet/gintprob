def conv_camelcase(input_str, capitalize_first=True):
    trimmed_name = input_str.strip()

    # Make sure we're only converting one name at a time.
    split_strs = trimmed_name.split()
    if len(split_strs) >= 2:
        err_fmt = 'ERROR: {0!r} must be split up into {1} separate calls.'
        err_msg = err_fmt.format(input_str, len(split_strs))
        raise ValueError(err_msg)

    # Keep track of leading and trailing underscores - they shouldn't go away.
    prefix_chars = '_' * (len(trimmed_name) - len(trimmed_name.lstrip('_')))
    suffix_chars = '_' * (len(trimmed_name) - len(trimmed_name.rstrip('_')))
    trimmed_name = trimmed_name.strip('_')

    # Any other underscores are indexes where words should be capitalized.
    str_words = trimmed_name.split('_')
    first_capital_index = 1 - bool(capitalize_first)
    for i in xrange(first_capital_index, len(str_words)):
        next_word = ''.join([str_words[i][0].upper(), str_words[i][1:]])
        str_words[i] = next_word
        # str_words[i] = str_words[i][0].upper() +
        # str_words[i] = str_words[i].capitalize()
    camelcase_name = ''.join(str_words)

    # Add any suffixes or prefixes we removed from the very beginning.
    camelcase_name = ''.join([prefix_chars, camelcase_name, suffix_chars])
    return camelcase_name
