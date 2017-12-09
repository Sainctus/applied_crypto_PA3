#!/usr/bin/env python
from Crypto.Util import number
import argparse
import sys
import os
import random
import binascii

################################################

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

################################################

def gencoprime(comp):
    for i in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if gcd(i, comp) == 1:
            return i
    return None

################################################

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

################################################

def main(pubFile, privFile, nBits):
    p = number.getPrime(int(nBits))
    q = number.getPrime(int(nBits))
    while q == p:
        q = number.getPrime(int(nBits))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = gencoprime(phi)

    d = modinv(e, phi)

    one = int(n).bit_length() 
    two = n
    thr = e
    fou = d

    f = open(pubFile, 'w')
    f.write(str(one) + "\n")
    f.write(str(two) + "\n")
    f.write(str(thr) + "\n")
    f.close()

    f = open(privFile, 'w')
    f.write(str(one) + "\n")
    f.write(str(two) + "\n")
    f.write(str(fou) + "\n")
    f.close


################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", help="Public key file", required=True)
    parser.add_argument("--s", help="Private key file", required=True)
    parser.add_argument("--n", help="Number of bits in N", required=True)
    args = parser.parse_args()

    main(args.p, args.s, args.n)

