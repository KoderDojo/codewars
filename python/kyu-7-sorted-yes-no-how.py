def is_sorted_and_how(arr):
    """
    Determines if an array of integers is sorted or not.
    If sorted, also determines if ascending or descending.

    A easy solution would be to just compare the array to
    versions that were sorted ascending and descending.
    However, that would run in O(nlogn) assuming a great
    sorting algorithm used by Python.

    This solution runs worst case O(n) and on average 0(1)
    because the arrays are typically full of unique integers.

    :param arr: array of integers with one correct answer.
    :return: str 'yes, ascending', 'yes, descending', or 'no'
    """
    if len(arr) == 2:
        if arr[0] != arr[1]:
            return 'yes, descending' if arr[0] > arr[1] else 'yes, ascending'

    first_number = arr[0]

    # need next unique number
    # to establish a direction of
    # ascending or descending
    i = 1
    while arr[i] == first_number:
        i += 1
    second_number = arr[i]

    direction = 'ascending' if first_number < second_number else 'descending'

    # established direction of sort.
    # if a change occurs, the array
    # is not sorted
    for j in range(i + 1, len(arr)):
        if (arr[j] > second_number and direction == 'descending') or (
                arr[j] < second_number and direction == 'ascending'):
            return 'no'

    # array must be sorted
    return 'yes, {}'.format(direction)


print(is_sorted_and_how([1, 2]))
print(is_sorted_and_how([15, 7, 3, -8]))
print(is_sorted_and_how([4, 2, 30]))
