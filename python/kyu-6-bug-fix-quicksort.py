"""
There is an implementation of quicksort algorithm.
Your task is to fix it. All inputs are correct.

Note: I couldn't go back and get the original broken
code to post here, but here is the fixed version of it.
"""


def quicksort(arr):
    if len(arr) < 1:
        return arr

    p = arr[0]

    return \
        (quicksort(list(filter(lambda x: x <= p, arr[1:])))
         + [p]
         + quicksort(list(filter(lambda x: x > p, arr[1:]))))
