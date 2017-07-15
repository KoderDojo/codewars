import random


def find_even_index(arr):
    sum_left = 0
    sum_right = sum(arr)

    for i in range(len(arr)):
        if i > 0:
            sum_left += arr[i - 1]
            sum_right -= arr[i - 1]

        sum_right -= arr[i]

        if sum_left == sum_right:
            return i

        sum_right += arr[i]

    return -1


array = random.sample(range(1000000), 100000)
print(find_even_index(array))

