def removNb(n):
    """
    This is just a mathematical formula.
    For each i in n, the other value must
    be (total - i) / (i + 1). We just need to make
    sure that other value is an integer
    and <= n. If so, we are good.
    :param n: int, where n > 0
    :return: list of tuples.
    """
    numbers = []

    total = sum(range(1, n+1))

    for i in range(1, n+1):
        # formula to find other number.
        j = (total - i) / (i + 1)

        # number must be an integer and <= n
        if j == int(j) and j <= n:
            numbers.append((i, int(j)))

    return numbers

print(removNb(26))