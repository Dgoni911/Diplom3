import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        logger.error(f"Function {func.__name__} failed after {max_attempts} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}. Retrying in {delay} sec...")
                    time.sleep(delay)
        return wrapper
    return decorator