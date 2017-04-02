#!/usr/bin/env python3

s = """.text:00010458                 ADD     R1, R0, #7
.text:0001045C                 SUB     R0, R1, #0x18
.text:00010460                 SUB     R0, R1, #0x1D
.text:00010464                 ADD     R0, R1, #8
.text:00010468                 ADD     R0, R1, #3
.text:0001046C                 SUB     R0, R1, #0x14
.text:00010470                 ADD     R0, R1, #0x18
.text:00010474                 SUB     R0, R1, #0xB
.text:00010478                 ADD     R0, R1, #4
.text:0001047C                 ADD     R0, R1, #0x11
.text:00010480                 ADD     R0, R1, #0x18
.text:00010484                 SUB     R0, R1, #0x1F
.text:00010488                 ADD     R0, R1, #4
.text:0001048C                 ADD     R0, R1, #0x12
.text:00010490                 ADD     R0, R1, #0x13
.text:00010494                 SUB     R0, R1, #0xD
.text:00010498                 ADD     R0, R1, #0xE
.text:0001049C                 SUB     R0, R1, #0x14
.text:000104A0                 MOV     R0, R1
.text:000104A4                 ADD     R0, R1, #0xA
.text:000104A8                 ADD     R0, R1, #4
.text:000104AC                 SUB     R0, R1, #0xD
.text:000104B0                 ADD     R0, R1, #7
.text:000104B4                 ADD     R0, R1, #8
.text:000104B8                 ADD     R0, R1, #0x12
.text:000104BC                 SUB     R0, R1, #0x12
.text:000104C0                 ADD     R0, R1, #0xD
.text:000104C4                 ADD     R0, R1, #4
.text:000104C8                 SUB     R0, R1, #0xE
.text:000104CC                 ADD     R0, R1, #0xE
.text:000104D0                 ADD     R0, R1, #0xB
.text:000104D4                 ADD     R0, R1, #0x15
.text:000104D8                 ADD     R0, R1, #4
.text:000104DC                 MOV     R0, R1
.text:000104E0                 ADD     R0, R1, #1
.text:000104E4                 ADD     R0, R1, #0xB
.text:000104E8                 ADD     R0, R1, #4
.text:000104EC                 SUB     R0, R1, #0x21
.text:000104F0                 ADD     R0, R1, #0xC
.text:000104F4                 ADD     R0, R1, #0x18
.text:000104F8                 SUB     R0, R1, #0x33
.text:000104FC                 ADD     R0, R1, #0x18
.text:00010500                 MOV     R0, R1
.text:00010504                 ADD     R0, R1, #7
.text:00010508                 ADD     R0, R1, #0xE
.text:0001050C                 ADD     R0, R1, #0xE
.text:00010510                 SUB     R0, R1, #0x33
.text:00010514                 ADD     R0, R1, #2
.text:00010518                 ADD     R0, R1, #0xE
.text:0001051C                 ADD     R0, R1, #0xC"""

regs = {
    'R0': 0x5A,
    'R1': None
}
for i, line in enumerate(s.split('\n')):
    tokens = line.split()
    op = tokens[1]
    dst = tokens[2].replace(',', '')
    src = tokens[3].replace(',', '')
    if op == 'ADD':
        regs[dst] = regs[src] + int(tokens[4][1:], 16)
    elif op == 'SUB':
        regs[dst] = regs[src] - int(tokens[4][1:], 16)
    elif op == 'MOV':
        regs[dst] = regs[src]
    else:
        raise Exception(op)
    
    if i > 0:
        print(chr(regs['R0']), end='')
print()

