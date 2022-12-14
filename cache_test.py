"""Example for a cache implementation using decorators."""

# Import built-in modules
import functools
import logging
import time

# Initializing our logger
logging.basicConfig()
_LOGGING_LEVEL = logging.DEBUG
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(_LOGGING_LEVEL)


def cached(function):
    """Use cached value or calculate and store the result in the cache.

    Args:
        function (function): Function to wrap.

    Returns:
        function: Wrapped caching function.

    """

    cache = {}

    @functools.wraps(function)
    def wrapper(*args):
        """Wrap executing the cache.

        Args:
            args (multiple): Arguments to use for calculation.

        Returns:
            function: Wrapped function to execute.

        """
        signature = (function, args)

        _LOGGER.debug("Using signature: %s", signature)

        if signature in cache:
            _LOGGER.debug("Retrieving from cache: %s", signature)
            result = cache[signature]
        else:
            _LOGGER.debug("Calculating: %s", signature)
            result = function(*args)
            _LOGGER.debug("Caching: %s", signature)
            cache[signature] = result

        return result

    return wrapper


@cached
def multiply(number):
    """Multiply a given number with itself.

    Args:
        number (int): The number to multiply with itself.

    Returns:
        int: The result of number * number.

    """
    time.sleep(3)
    return number * number


@cached
def add(number_a, number_b):
    """Add the given numbers.

    Args:
        number_a (int): The first number to use for calculation.
        number_b (int): The second number to use for calculation.

    Returns:
        int: The sum of the given numbers

    """
    time.sleep(3)
    return number_a + number_b


print(add(4, 5))
