def fold_array(array, runs):

    def fold(array, low, high):
        if low == high:
            return [array[low]]

        if low >= high:
            return []

        return [array[low] + array[high]] + fold(array, low+1, high-1)

    if len(array) < 2:
        return array

    arr = array

    for i in range(runs):
        low = 0
        high = len(arr) - 1
        arr = fold(arr, low, high)

    return arr

array = [1, 2, 3, 4, 5]
print(fold_array(array, 3))
print(array)
