from typing import Tuple
import math
import time
from random import randrange


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


def g(n, x):
    return x ** 2 + 1 % n


def factorize(n):
    x = 2
    y = 2
    d = 1

    while d == 1:
        x = g(n, x)
        y = g(n, g(n, y))
        d = math.gcd(abs(x - y), n)

    if d == n:
        return None
    else:
        return d




def rho(n, c):
    t = 2;
    h = 2;
    d = 1;

    while d == 1:
        t = (t*t + c) % n
        h = (h*h + c) % n
        h = (h*h + c) % n
        d = math.gcd(t-h, n)

    if d == n:
        return rho(n, c+1);
    else:
        return d;


def wheel(n):
    ws = [1,2,2,4,2,4,2,4,6,2,6]
    f = 2
    w = 0

    while (f * f <= n):
        if (n % f == 0):
            print(f)
            n = n // f
        else:
            f += ws[w]
            if w == 10:
                w = 3
            else:
                w += 1

    print(n)

    return 0


squares = []
for i in range(1,100):
    squares.append(i * i)


def factorize_squares(n):
    f = 1
    for i in squares:
        if n % i == 0:
            f *= i
            n //= i

    return f, n


# 1.6s
t = 821844181995567608861526435749234500883998



# Reminder is not three-squarable so calculation takes a very long time if you don't check for this
t = 821844181995567608861526435749234500883999





# t = 12345678910123653532


# wheel(t)

# 1/0

# while True:
    # f = rho(t, 1)

    # if f is None:
        # print(t)
        # break
    # else:
        # print(f)
        # t = t // f


# # print(factorize(t))



# 1/0



start = time.time()

# n = 4k + 2
t = 821844181995567608861526435749234500883998
print("=======================================")
print(t)

a = randrange(1, math.isqrt(t))
b = randrange(1, math.isqrt(t - a * a))

p = t - a * a - b * b

r = (p - 1) // 4

x = randrange(1, p)
1/0





# Should use fast exponentiation
m = (x ** 2) ** r






# a, b, c, d = four_squares(t)

print(a*a + b*b + c*c + d*d)






duration = time.time() - start
print(f"=====> {duration}")









