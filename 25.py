from fnmatch import *


def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


k = 0
n = 2352000
while k < 5:
    n += 1
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                a.add(i)
            if is_prime(n // i):
                a.add(n // i)
    s = ""
    for i in sorted(a):
        s += str(i)
    if fnmatch(s, "10*29"):
        print(n, max(a))
        k += 1
