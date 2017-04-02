#!/usr/bin/env python3

mem = list(open('shellcode', 'rb').read())
out = [0] * 0x100

eax = 0
ebx = 0x146
ecx = 8
for i in range(ecx):
    dl = mem[ebx]
    #mem[eax] = dl
    out[eax] = dl
    eax += 2
    ebx += 1

ebx = 0x14E
eax = 1
for i in range(7):
    dl = mem[ebx]
    out[eax] = dl
    eax += 2
    ebx += 1

print("".join([chr(o) for o in out]))
