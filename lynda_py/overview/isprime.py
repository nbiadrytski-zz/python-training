#!/usr/bin/env python3


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % 2 == 0:
            return False
    else:
        return True


def list_primes():
    for i in range(100):
        if isprime(i):
            print(i, end=' ', flush=True)
    print()


n = 5
if isprime(n):
    print('{} is prime'.format(n))
else:
    print('{} is not prime'.format(n))

list_primes()
