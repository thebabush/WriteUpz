#!/usr/bin/env python3
 
mm = [
    0x77, 0x56, 0x76, 0x5F, 0x3D, 0x52, 0x7B, 0x43, 0x53, 0x58, 0x67, 0x19,
    0x67, 0x58, 0x7C, 0x55
]

aa = []
for i in range(len(mm)//2):
    aa.append((mm[i*2]<<8)|mm[i*2+1])
aa = aa[::-1]

alphabet = '1234567890qwertyuiopasdfghjklzxcvbnm.@'

# Loop to search for printable strings
for k in range(0x10000):
    cc = []
    nope = 0
    for i, a in enumerate(aa):
        n = k^a
        c0 = chr(n >> 8)
        c1 = chr(n & 0xFF)
        if c0 not in alphabet:
            nope = 1
            break
        if c1 not in alphabet:
            nope = 1
            break
        cc.append(c0)
        cc.append(c1)

    if nope == 0:
        # No unprintable characters in this string
        print("K:", hex(k))
        print("Flag: ", end='')
        for a, b in zip(cc[1::2], cc[::2]):
            print(a, end='')
            print(b, end='')
        print()

