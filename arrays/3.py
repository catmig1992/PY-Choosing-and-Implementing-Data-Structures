import numpy as np

a = np.array([1, 2, 3, 4, 5])

def multiply_by_3(arr):
    return 3 * arr

def multiply_by(arr, num = 1):
    return num * arr

print(multiply_by_3(a))
print(multiply_by(a, 5))
print(multiply_by(a, 10))
print(multiply_by(a, 10000))
