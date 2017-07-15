import random


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

array = random.sample(range(1000000), 30000)
print(find_even_index(array))
