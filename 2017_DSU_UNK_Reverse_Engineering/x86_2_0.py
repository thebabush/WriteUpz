#!/usr/bin/env python3

res = [ord(c) for c in r'yfoR|a~}']
key = [0xD, 0xE, 0xA, 0xD, 0xC, 0, 0xD, 0xE]

for r, k in zip(res[::-1], key * 10):
    print(chr(r ^ k), end='')
print()

