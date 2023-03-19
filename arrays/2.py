import numpy as np

a = np.array([1, 2, 3, 4, 5])

def array_sum(arr):
    result = 0
    for i in arr:
        result += i
    return result

print(array_sum(a))
