import time

def timer(original_function):
    def wrapper(*args, **kwargs):
        before = time.process_time()
        result = original_function(*args, **kwargs)
        after = time.process_time()
        print(f"{original_function.__name__} took {after - before} seconds")
        return result
    return wrapper

terms = 9999999
power = 3
threshold = 582375482375

def cubes_generator(): return (x ** power for x in range(terms))
def cubes_list(): return [x ** power for x in range(terms)]

@timer
def find_cube(cubes_function):
    for cube in cubes_function():
        if cube > threshold:
            print(f"{cube} is the first number above {threshold}")
            break
    else: 
        print("No cubed number found above threshold")

find_cube(cubes_generator)
find_cube(cubes_list)