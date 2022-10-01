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
# https://mathoverflow.net/questions/259152/efficient-method-to-write-number-as-a-sum-of-four-squares
t = 821844181995567608861526435749234500883998


t = 4 * 2**1000 + 14

print("=======================================")
print(t)


m = 1
p = 5

while m * m % p != p - 1:
    a_max = math.isqrt(t)

    for a in range(a_max, -1, -1):
        if not three_squarable(t - a * a):
            continue
        else:
            break

    # print("eeeeeeeeeeeeeee")
    # print(t - a * a)

    # Should actually have one odd and one even and test for it here but seems to work downstreams anyway
    # a = randrange(1, math.isqrt(t))
    b = randrange(1, math.isqrt(t - a * a))

    p = t - a * a - b * b

    r = (p - 1) // 4

    x = randrange(1, p)

    # print("-----")
    # print(x)
    # print(r)


    e = r
    y = 1

    while e > 1:
        if e % 2 == 0:
            x = x * x % p
            e = e // 2
        else:
            y = y * x % p
            x = x * x % p
            e = (e - 1) // 2

    x = x * y % p

    m = x


print("------------------------")
print(m)
print(p)
print(p - 1 - (m * m % p))




# no = (m * m + 1) // p   # Exact division by p

# print(no)
# print(m * m + 1 - p * no)

c = p
d = m
r = p
while c > math.sqrt(p):
    r = c - (c // d) * d
    c = d
    d = r

print("EUCLIDE DONE")
print(p - c * c - d * d)



print("RESULT")
print(t - a ** 2 - b ** 2 - c ** 2 - d ** 2)


# print(m)


# print("%%%%%%%")
# print(m * m % p)
# print(p - 1)




# a, b, c, d = four_squares(t)

print(a*a + b*b + c*c + d*d)






duration = time.time() - start
print(f"=====> {duration}")









