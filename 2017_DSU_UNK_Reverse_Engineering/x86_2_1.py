#!/usr/bin/env python

import os

s = '@'
cmd = '''echo {} | wine 2_mod.exe | tail -n +3 | head -n -1 > /tmp/fuck.txt'''

def run(s):
    os.system(cmd.format(s))
    out = [s.strip() for s in open('/tmp/fuck.txt', 'r').readlines()][-1]
    a, _, b = out.split()
    return a == b

alphabet = '1234567890qwertyuiopasdfghjklzxcvbnm.@QWERTYUIOPASDFGHJKLZXCVBNM'
for i in range(10):
    for c in alphabet:
        if run(s+c):
            s += c
            print s
            break

