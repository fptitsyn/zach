from functools import lru_cache


def next_prime(n):
    while True:
        n += 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            return n


def next_prod(n):
    while True:
        n += 1
        for i in range(2, 14):
            if n == 2 ** i:
                return n


@lru_cache()
def f(x, y):
    if x == y:
        return 1
    if x > y or x == 3 or x == 14:
        return 0
    if x % 10 == 0:
        return f(x + next_prime(x), y) + f(x + next_prime(x), y)
    return f(x + next_prime(x), y) + f(x + next_prime(x), y) + f(x + x % 10, y)


print(f(2, 1024) * f(1024, 3072))
