import inspect
import logging
import functools
import types


def logCall(func=None, filename=None, level=None):

    def decorator(function):

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(filename)
            if not logger.handlers:
                handler = logging.StreamHandler()
                formatter = logging.Formatter(fmt=logging.BASIC_FORMAT)
                handler.setFormatter(formatter)
                logger.addHandler(handler)
            if isinstance(level, basestring):
                loggerLevel = logging._levelNames.get(level.lower(), level)
            elif level is not None:
                loggerLevel = level
            else:
                loggerLevel = logger.getEffectiveLevel()
            logger.log(loggerLevel, 'Calling %r (args:%r, kwargs:%r)...', function, args, kwargs)
            retVal = function(*args, **kwargs)
            logger.log(loggerLevel, '-> Returned object: %r', retVal.__class__)
            return retVal

        spec = inspect.getargspec(function)
        if len(spec.args) > 1 or spec.varargs or spec.keywords:
            return wrapper
        else:
            return functools.wraps(function)(wrapper)
    if isinstance(func, types.FunctionType):
        return decorator(func)
    else:
        return decorator
