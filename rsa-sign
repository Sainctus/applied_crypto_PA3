#!/usr/bin/env python
import argparse
import sys
import os
import random
import string
import binascii



def main(keyFile, inFile, outFile):
    ###########################################
    #Read key info from file#
    
    f = open(keyFile, 'r')

    nBits = string.rstrip(f.readline(), "\n")
    nBits = int(nBits)
    
    n = string.rstrip(f.readline(), "\n")
    n = int(n)
    
    e = string.rstrip(f.readline(), "\n")
    e = int(e)
    
    f.close()

    ###########################################
    #Generate randomness#

    r = random.getrandbits(int(nBits/2))
    r = bytes(r)
    r = str(r)

    while 1:
        if r.find('0') != -1:
            tmp = str(random.randint(1, 9))
            r = string.replace(r, '0', tmp, 1)
        else:
            break
   
    r = bytes(r)
    rand = b"0" + b"2" + r + b"0"

    ###########################################
    #Read message from file#
    
    f = open(inFile, 'r')
    m = string.rstrip(f.readline(), "\n")
    f.close()

    ###########################################
    #Concat and encrypt#
    
    enc = rand + bytes(m)
    enc = int(enc)

    final = pow(enc, e, n)

    ###########################################
    #Write result to file#
    
    f = open(outFile, 'w')
    f.write(str(final))
    f.close()

    ###########################################


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", help="Key file", required=True)
    parser.add_argument("--i", help="Input file", required=True)
    parser.add_argument("--o", help="Output file", required=True)
    args = parser.parse_args()

    main(args.k, args.i, args.o)
