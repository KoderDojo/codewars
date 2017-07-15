memo = {0: 0, 1: 1}


def fib(n):
    """
    Calculate Fibonacci numbers.
    Improve performance by using memoization.

    :param n: int, the nth Fibonacci number.
    :return: int, the value of the nth Fibonacci number.
    """
    if n in memo:
        return memo[n]

    answer = fib(n - 1) + fib(n - 2)
    memo[n] = answer

    return answer


def productFib(prod):
    """
    Returns an array containing the two consecutive Fibonacci
    numbers whose product are either equal to or just greater
    than the product provided as an argument. If the product
    of the two Fibonacci numbers is equal to the product, we
    include True in the array, otherwise, False.

    :param prod: int, an arbitrary integer
    :return: list. a list of two consecutive Fibonacci numbers
        and either True or False. e.g. [Fib(i), Fib(i+1), True]
    """
    i = 0
    value = fib(i) * fib(i + 1)

    while value < prod:
        i += 1
        value = fib(i) * fib(i + 1)

    return [fib(i), fib(i+1), True] if value == prod else [fib(i), fib(i+1), False]


print(productFib(800))
