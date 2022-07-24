import itertools

array = [3, 6, 9, 12, 15, 4, 2, 1, 30]
it = itertools.combinations(array, 2)
target = 15

def any_lambda(iterable, function):
  return any(function(i) for i in iterable)

def sum2(comb):
    if (sum(comb) == target):
        print(f"target: {target} found using {comb}")
        return True

print(any_lambda(it, sum2))


# for comb in it:
#     if sum(comb) == target:
#         print(f"target: {target} found using {comb}")
#         break

# # if no break
# else:
#     print("target not found")