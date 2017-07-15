def count_Kprimes(k, start, nd):
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    kprimes = []

    for i in range(start, nd + 1):
        if len(prime_factors(i)) == k:
            kprimes.append(i)

    return kprimes


def puzzle(s):
    one_prime = count_Kprimes(1, 1, s)
    three_prime = count_Kprimes(3, 1, s)
    seven_prime = count_Kprimes(7, 1, s)

    solutions = [(a, b, c) for a in one_prime for b in three_prime for c in seven_prime if a + b + c == s]
    return len(solutions)

print(puzzle(143))

