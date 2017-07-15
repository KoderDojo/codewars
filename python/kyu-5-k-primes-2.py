from math import floor, sqrt


def fac(n):
    step = lambda x: 1 + (x << 2) - ((x >> 1) << 1)
    maxq = int(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n // q) or [n]


def nfac(n):
    m = int(floor(sqrt(n)))
    q, d = 2 + (n & 1), 1
    while q <= m and n % q != 0:
        q, d = 1 + (d << 2) - (d - (d & 1)), d + 1

    return q > m and 1 or 1 + nfac(n//q)

print(fac(100))

# https://rosettacode.org/wiki/Prime_decomposition#Python:_Using_floating_point