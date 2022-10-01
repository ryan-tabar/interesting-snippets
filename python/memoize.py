# A decorator to that caches results that are expensive to compute
# (Only pratical for pure functions)
def memoize(original_function):
    cache = {}
    def wrapper(*args, **kwargs):
        stringed_args = f"{args}{kwargs}"
        try:
            return cache[stringed_args]
        except:
            cache[stringed_args] = original_function(*args, **kwargs)
            return cache[stringed_args]
    wrapper.__name__ = original_function.__name__
    return wrapper


# Example on the fibonacci sequence
if __name__ == "__main__":

    @memoize
    def fib(n): 
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    print(fib(32))
