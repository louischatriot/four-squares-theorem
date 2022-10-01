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



def check_answer(t, a, b, c, d):
    print("RESULT")
    print(a)
    print(b)
    print(c)
    print(d)

    res = t - a * a - b * b - c * c - d * d
    print("CHECK")
    print(res)

    if res != 0:
        print("FAIL")


def four_square_brute_force(n):
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


def four_square_4n_2(t):
    if t % 4 != 2:
        raise BaseException("t should be of form 4k+2")

    m = 1
    p = 5

    a_max = math.isqrt(t)

    for a in range(a_max, -1, -1):
        if not three_squarable(t - a * a):
            continue
        else:
            break

    # The 1000 is arbitrary here but we want to avoid special case where b cannot be found because t - a * a is too small
    if t - a * a < 1000:
        return four_square_brute_force(t)

    b = math.isqrt(t - a * a)   # b_max + 1

    while m * m % p != p - 1:
        # Should actually have one odd and one even and test for it here but seems to work downstreams anyway
        # a = randrange(1, math.isqrt(t))
        b -= 1
        # b = randrange(1, math.isqrt(t - a * a))
        p = t - a * a - b * b
        r = (p - 1) // 4
        x = randrange(1, p)

        # Find our m
        # See https://mathoverflow.net/questions/259152/efficient-method-to-write-number-as-a-sum-of-four-squares
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

    # Euclidian division until we reach sqrt(p)
    # See https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares#Algorithm
    c = p
    d = m
    r = p
    while c > math.sqrt(p):
        r = c - (c // d) * d
        c = d
        d = r

    return (a, b, c, d)


def four_square_4n_1_or_3(n):
    if n % 4 != 1 and n % 4 != 3:
        raise BaseException("n should be of form 4k+& or 4k+3")

    l = four_square_4n_2(2 * n)

    evens = []
    odds = []
    for i in l:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    _a, _b = odds
    _c, _d = evens
    a = (_a + _b) // 2
    b = (_a - _b) // 2
    c = (_c + _d) // 2
    d = abs(_c - _d) // 2

    return a, b, c, d


start = time.time()

# https://mathoverflow.net/questions/259152/efficient-method-to-write-number-as-a-sum-of-four-squares

# n = 4k + 2
# t = 821844181995567608861526435749234500883998

# 4k + 2
# t = 42860344287450692837937001962400072422456192468221344297750015534814042044997444899727935152627834325103786916702125873007485811427692561743938310298794299215738271099296923941684298420249484567511816728612185899934327765069595070236662175784308251658284785910746168670641719326610497547348822672277518

# 4k + 2
# t = 171441377149802771351748007849600289689824769872885377191000062139256168179989779598911740610511337300415147666808503492029943245710770246975753241195177196862953084397187695766737193680997938270047266914448743599737311060278380280946648703137233006633139143642984674682566877306441990189395290689112074

# print("=======================================")
# print(t)

# a, b, c, d = four_square_4n_2(t)

# duration = time.time() - start
# print(f"=====> {duration}")


start = time.time()

# 4k + 1
t = 685765508599211085406992031398401158759299079491541508764000248557024672719959118395646962442045349201660590667234013968119772982843080987903012964780708787451812337588750783066948774723991753080189067657794974398949244241113521123786594812548932026532556574571938698730267509225767960757581162756448297

print("=======================================")
print(t)

a, b, c, d = four_square_4n_1_or_3(t)
check_answer(t, a, b, c, d)

duration = time.time() - start
print(f"=====> {duration}")




