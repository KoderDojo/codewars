memo = {1: 45}


def sum_dif_rev(n):
    """
    Finds the nth number that summed
    with its number reversed is evenly
    divisible by the difference of the
    two.

    :param n: int - nth number to find
    :return: int - the value of the nth number
    """
    # If we already found the nth number,
    # just return it from the cache.
    if n in memo:
        return memo[n]

    # We haven't found the nth number.
    # Start with the highest number
    # we do have in the cache.
    i = max(memo.keys())
    current_number = memo[i]

    while i < n:
        current_number += 1

        # instructions state to not include
        # numbers that when reversed start
        # with 0. This would be multiples of 10.
        if current_number % 10 == 0:
            continue

        current_number_reversed = int(str(current_number)[::-1])

        # Exclude numbers that are same forwards
        # and backwards to avoid division by zero.
        if current_number == current_number_reversed:
            continue

        # Found the next number. Store it in cache.
        if (current_number + current_number_reversed) %\
                abs(current_number - current_number_reversed) == 0:
            i += 1
            memo[i] = current_number

    return current_number


print(sum_dif_rev(4))
for l in range(1, 66):
    print(sum_dif_rev(l))
