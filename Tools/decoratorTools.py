import inspect
import logging
import time
from functools import wraps

from Tools.Interfaces import BASE_DIR
logging.getLogger(__name__)

def using_timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = function(*args, **kwargs)
        t2 = time.time()
        logging.debug('\n{}(): Total time: {:.4} s'.format(function.__name__, t2 - t1))
        return result

    return wrapper


def using_tryCatch(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
            return result
        except Exception as e:
            error_file = inspect.getfile(function)
            error_file = error_file.replace(BASE_DIR, '')
            line = e.__traceback__.tb_lineno
            func_name = function.__name__
            logging.error(f'------------ [{error_file}] : [line {line}] ----- [{func_name}()] ----- [{e}] ------------')

    return wrapper


def using_logging(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        logging.debug(f"----- {function.__name__}: start -----")
        output = function(*args, **kwargs)
        logging.debug(f"----- {function.__name__}: end -----")
        return output

    return wrapper


def repeat(number_of_times):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(number_of_times):
                func(*args, **kwargs)

        return wrapper

    return decorate


def retry(num_retries, exception_to_check, sleep_time=0):
    """
    如果函数引发特定异常则重试函数执行的装饰器。
    """

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, num_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    print(f" {func.__name__}引发{e.__class__.__name__} Retry...")
                    if i < num_retries:
                        time.sleep(sleep_time)
                        # 如果函数在指定次数的重试后不成功，则引发异常
            raise e

        return wrapper

    return decorate


# --------------------------------------------------------------


if __name__ == '__main__':
    ...
