from typing import Tuple
import math
import time



def largest_square_lower_than(n):
    tranch_size = 16

    digits = int(math.log10(n))

    big = int(digits / tranch_size)

    _n = int(n / 10 ** (big * tranch_size))

    res = int(math.sqrt(_n))

    res = res * int(10 ** (big * tranch_size / 2))


    print(n)
    print(res * res)


    return res


def four_squares(n: int) -> Tuple[int, int, int, int]:
    a_max = math.isqrt(n)

    for a in range(a_max, -1, -1):
        if not three_squarable(n - a * a):
            continue

        b_max = math.isqrt(n - a * a)

        for b in range(b_max, -1, -1):
            c_max = math.isqrt(n - a * a - b * b)

            for c in range(c_max, -1, -1):
                sr = n - a * a - b * b - c * c
                d = math.isqrt(sr)
                if sr == d * d:
                    return (a, b, c, d)


def three_squarable(n):
    if n == 0:
        return True

    while n % 4 == 0:
        n = n / 4

    return (n % 8 != 7)





# 1.6s
t = 821844181995567608861526435749234500883998



# Reminder is not three-squarable so calculation takes a very long time if you don't check for this
t = 821844181995567608861526435749234500883999



start = time.time()

print("=======================================")
print(t)

a, b, c, d = four_squares(t)

print(a*a + b*b + c*c + d*d)

duration = time.time() - start
print(f"=====> {duration}")


1/0




def squares(n, n_squares):
    a_max = int(math.sqrt(n))

    if n_squares == 1:
        if a_max * a_max == n:
            return a_max
        else:
            return None

    for a in range(a_max, 0, -1):
        b = squares(n - a * a, n_squares - 1)
        if b is None:
            continue
        else:
            return (a_max, b)   # Should unpack tuple



