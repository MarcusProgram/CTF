#!/usr/bin/python

from binascii import hexlify
from Crypto.Util.number import getStrongPrime, bytes_to_long
import math
import os
import sys

if sys.version_info < (3, 9):
    import gmpy2
    math.gcd = gmpy2.gcd
    math.lcm = gmpy2.lcm

FLAG  = open('flag.txt').read().strip()
FLAG  = int(hexlify(FLAG.encode()), 16)
SEED  = int(hexlify(os.urandom(32)).decode(), 16)


p = getStrongPrime(1024)
q = getStrongPrime(1024)

x = p + q
n = p * q

e = 65537

m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)

c = pow(FLAG, e, n)

print(f'x = {x}')
print(f'n = {n}')
print(f'c = {c}')
