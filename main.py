import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


assert is_prime(2)
assert is_prime(3)
assert is_prime(7)
assert is_prime(13)

assert not is_prime(1)
assert not is_prime(4)
assert not is_prime(9)
assert not is_prime(15)

print("All tests passed!")
