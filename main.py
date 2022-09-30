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
    # a_max = int(math.sqrt(n))
    a_max = int(n ** .5)

    for a in range(a_max, -1, -1):
        if a * a > n:
            continue

        b_max = int((n - a * a) ** .5)

        for b in range(b_max, -1, -1):
            if b * b > n - a * a:
                continue

            c_max = int((n - a * a - b * b) ** .5)

            for c in range(c_max, -1, -1):
                sr = n - a * a - b * b - c * c
                d = int(sr ** .5)
                if sr == d * d:
                    return (a, b, c, d)







    
t = 821844181995577608861826435749234500883999

print(int(t ** .5))
1/0

start = time.time()


a, b, c, d = four_squares(t)
a, b, c, d = four_squares(t)
a, b, c, d = four_squares(t)

print(a)
print(b)
print(c)
print(d)

print("tttttttttttttttttt")
print(t)
print(a*a + b*b + c*c + d*d)

duration = time.time() - start
print(f"=====> {duration}")






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



