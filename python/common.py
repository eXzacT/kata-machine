from typing import Callable
from functools import wraps
from time import perf_counter


def time_execution(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        result = func(*args, **kwargs)
        time_end = perf_counter()
        print(
            f"\n{func.__name__} took {(time_end-time_start)*1000:>10.4f}ms to complete.")
        return result

    return wrapper
