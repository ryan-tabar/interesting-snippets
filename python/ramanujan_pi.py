# Ramanujan's pi formula
# https://www.cronodon.com/Programming/Pi.html

import math as m

def summation(N):
    total = 0
    for n in range(N):
        numerator = m.factorial(4 * n) * (1103 + 26390 * n)
        denominator = m.pow(m.factorial(n), 4) * m.pow(396, 4 * n)
        total += numerator / denominator
    return total

def pi(N):
    constant = 2 * m.sqrt(2) / 9801
    result = constant * summation(N)
    return 1 / result

def print_pi(N):
    result = pi(N)
    print(f"result: {result}, accuracy: {m.pi/result:.15%}")

print_pi(2)