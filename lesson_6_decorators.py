import time


def timeit(func):
    def wrapper(*args):
        start_time = time.time()  # Capture the start time before the function call
        func(*args)  # Call the function
        end_time = time.time()  # Capture the end time after the function call
        print(
            f"Time taken by {func.__name__} function: {end_time - start_time} seconds"
        )

    return wrapper


@timeit
def test_function(seconds: int):
    time.sleep(seconds)


test_function(3)
