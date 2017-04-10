#!/usr/bin/env python3

import sys

cm = {}
rm = {
    0x50: '<end>'
}
for i in range(ord('A'), ord('Z')+1):
    cm[chr(i)] = 0x80 + i - ord('A')
    rm[0x80 + i - ord('A')] = chr(i)
for i in range(ord('a'), ord('z')+1):
    cm[chr(i)] = 0xA0 + i - ord('a')
    rm[0xA0 + i - ord('a')] = chr(i)
for i in range(10):
    rm[0xF6+i] = '*{}*'.format(i)

if len(sys.argv) < 3:
    print("Nope")
    exit()

if sys.argv[2] != '-':
    s = sys.argv[2]
else:
    s = input('> ')

if sys.argv[1] == 'decode':
    for cc in s.split():
        c = rm[int(cc, 16)]
        print(c, end='')
    print()
else:
    for c in s:
        print("{:02X}".format(cm[c]), end=" ")
    print()

