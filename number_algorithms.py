# number_algorithms.py
# Number algorithms: square root, smallest divisor, GCD, primes, prime factors.


# Square root of n (n >= 0) using Newton's method.
# The guess is improved until two guesses are almost equal.
def square_root(n):
    if n == 0:
        return 0
    guess = n / 2
    better = (guess + n / guess) / 2
    while abs(guess - better) > 0.000001:
        guess = better
        better = (guess + n / guess) / 2
    return round(better, 4)


# Smallest divisor of n (n >= 2) greater than 1.
# Only divisors up to the square root of n need to be tried.
def smallest_divisor(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            break
        d += 1
    else:
        return n                 # no divisor found, so n is prime
    return d


# Greatest common divisor using Euclid's algorithm.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# All prime numbers from 2 up to n.
# A number is prime when its smallest divisor is the number itself.
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if smallest_divisor(num) == num:
            primes.append(num)
    return primes


# Prime factors of n (n >= 1), smallest first. Example: 60 -> [2, 2, 3, 5]
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n = n // d
        else:
            d += 1
    if n > 1:
        factors.append(n)
    return factors
