#!/usr/bin/env python3

s = """.text:000105BC                 ADD     R0, R1, #0xC
.text:000105C0                 LDR     LR, [SP],#4
.text:000105C4                 BX      LR
.text:000105C8 ; ---------------------------------------------------------------------------
.text:000105C8                 ADD     R0, R1, #0xE
.text:000105CC                 LDR     LR, [SP],#4
.text:000105D0                 BX      LR
.text:000105D4 ; ---------------------------------------------------------------------------
.text:000105D4                 ADD     R0, R1, #2
.text:000105D8                 LDR     LR, [SP],#4
.text:000105DC                 BX      LR
.text:000105E0 ; ---------------------------------------------------------------------------
.text:000105E0                 SUB     R0, R1, #0x33
.text:000105E4                 LDR     LR, [SP],#4
.text:000105E8                 BX      LR
.text:000105EC ; ---------------------------------------------------------------------------
.text:000105EC                 ADD     R0, R1, #4
.text:000105F0                 LDR     LR, [SP],#4
.text:000105F4                 BX      LR
.text:000105F8 ; ---------------------------------------------------------------------------
.text:000105F8                 ADD     R0, R1, #0xB
.text:000105FC                 LDR     LR, [SP],#4
.text:00010600                 BX      LR
.text:00010604 ; ---------------------------------------------------------------------------
.text:00010604                 ADD     R0, R1, #6
.text:00010608                 LDR     LR, [SP],#4
.text:0001060C                 BX      LR
.text:00010610 ; ---------------------------------------------------------------------------
.text:00010610                 ADD     R0, R1, #8
.text:00010614                 LDR     LR, [SP],#4
.text:00010618                 BX      LR
.text:0001061C ; ---------------------------------------------------------------------------
.text:0001061C                 MOV     R0, R1
.text:00010620                 LDR     LR, [SP],#4
.text:00010624                 BX      LR
.text:00010628 ; ---------------------------------------------------------------------------
.text:00010628                 ADD     R0, R1, #0x13
.text:0001062C                 LDR     LR, [SP],#4
.text:00010630                 BX      LR
.text:00010634 ; ---------------------------------------------------------------------------
.text:00010634                 ADD     R0, R1, #7
.text:00010638                 LDR     LR, [SP],#4
.text:0001063C                 BX      LR
.text:00010640 ; ---------------------------------------------------------------------------
.text:00010640                 SUB     R0, R1, #0x21
.text:00010644                 LDR     LR, [SP],#4
.text:00010648                 BX      LR
.text:0001064C ; ---------------------------------------------------------------------------
.text:0001064C                 ADD     R0, R1, #0x16
.text:00010650                 LDR     LR, [SP],#4
.text:00010654                 BX      LR
.text:00010658 ; ---------------------------------------------------------------------------
.text:00010658                 SUB     R0, R1, #0x15
.text:0001065C                 LDR     LR, [SP],#4
.text:00010660                 BX      LR
.text:00010664 ; ---------------------------------------------------------------------------
.text:00010664                 ADD     R0, R1, #1
.text:00010668                 LDR     LR, [SP],#4
.text:0001066C                 BX      LR
.text:00010670 ; ---------------------------------------------------------------------------
.text:00010670                 SUB     R0, R1, #0x1F
.text:00010674                 LDR     LR, [SP],#4
.text:00010678                 BX      LR"""

# Parse the string and record the pair (function address, +/-value)
ks = []
for line in s.split('\n')[::4]:
    tokens = line.split()
    k = None
    op = tokens[1]
    arg = tokens[-1]
    if op == 'ADD':
        k = 1
    elif op == 'SUB':
        k = -1
    elif op == 'MOV':
        k = 0
    arg = int(arg[1:], 16)
    ks.append(k * arg)

s = """MOV     R11, R10
STR     R11, [SP,#4+var_8]!
ADD     R11, R10, #0xC
STR     R11, [SP,#8+var_C]!
ADD     R11, R10, #0x18
STR     R11, [SP,#0xC+var_10]!
ADD     R11, R10, #0x24
STR     R11, [SP,#0x10+var_14]!
ADD     R11, R10, #0x30
STR     R11, [SP,#0x14+var_18]!
ADD     R11, R10, #0x3C
STR     R11, [SP,#0x18+var_1C]!
ADD     R11, R10, #0x48
STR     R11, [SP,#0x1C+var_20]!
ADD     R11, R10, #0xC
STR     R11, [SP,#0x20+var_24]!
ADD     R11, R10, #0xC
STR     R11, [SP,#0x24+var_28]!
ADD     R11, R10, #0x48
STR     R11, [SP,#0x28+var_2C]!
ADD     R11, R10, #0x24
STR     R11, [SP,#0x2C+var_30]!
ADD     R11, R10, #0x3C
STR     R11, [SP,#0x30+var_34]!
ADD     R11, R10, #0x54
STR     R11, [SP,#0x34+var_38]!
ADD     R11, R10, #0x60
STR     R11, [SP,#0x38+var_3C]!
MOV     R11, R10
STR     R11, [SP,#0x3C+var_40]!
ADD     R11, R10, #0x6C
STR     R11, [SP,#0x40+var_44]!
ADD     R11, R10, #0xC
STR     R11, [SP,#0x44+var_48]!
ADD     R11, R10, #0x78
STR     R11, [SP,#0x48+var_4C]!
ADD     R11, R10, #0x84
STR     R11, [SP,#0x4C+var_50]!
ADD     R11, R10, #0x90
STR     R11, [SP,#0x50+var_54]!
ADD     R11, R10, #0x60
STR     R11, [SP,#0x54+var_58]!
ADD     R11, R10, #0x9C
STR     R11, [SP,#0x58+var_5C]!
ADD     R11, R10, #0xA8
STR     R11, [SP,#0x5C+var_60]!
ADD     R11, R10, #0xC
STR     R11, [SP,#0x60+var_64]!
ADD     R11, R10, #0x9C
STR     R11, [SP,#0x64+var_68]!
ADD     R11, R10, #0xA8
STR     R11, [SP,#0x68+var_6C]!
ADD     R11, R10, #0xC
STR     R11, [SP,#0x6C+var_70]!
ADD     R11, R10, #0xB4
STR     R11, [SP,#0x70+var_74]!
ADD     R11, R10, #0x78
STR     R11, [SP,#0x74+var_78]!
ADD     R11, R10, #0x60
STR     R11, [SP,#0x78+var_7C]!
ADD     R11, R10, #0x3C
STR     R11, [SP,#0x7C+var_80]!
ADD     R11, R10, #0xB4
STR     R11, [SP,#0x80+var_84]!
ADD     R11, R10, #0xA8
STR     R11, [SP,#0x84+var_88]!
ADD     R11, R10, #0x60
STR     R11, [SP,#0x88+var_8C]!
ADD     R11, R10, #0x3C
STR     R11, [SP,#0x8C+var_90]!
ADD     R11, R10, #0xA8
STR     R11, [SP,#0x90+var_94]!
ADD     R11, R10, #0x78
STR     R11, [SP,#0x94+var_98]!
ADD     R11, R10, #0x60
STR     R11, [SP,#0x98+var_9C]!
ADD     R11, R10, #0x3C
STR     R11, [SP,#0x9C+var_A0]!
ADD     R11, R10, #0xA8
STR     R11, [SP,#0xA0+var_A4]!"""

# Emulate the code and unfold the ROP chain
regs = {
    'R0': 0x5A,
    'R1': 0x5A+7,
    'R10': 0,
    'R11': 0
}
mem = []
for line in s.split('\n'):
    tokens = line.split()
    op = tokens[0]
    dst = tokens[1].replace(',', '')
    try:
        src = tokens[2].replace(',', '')
    except IndexError:
        src = None
    if op == 'ADD':
        regs[dst] = regs[src] + int(tokens[3][1:], 16)
    elif op == 'SUB':
        regs[dst] = regs[src] - int(tokens[3][1:], 16)
    elif op == 'MOV':
        regs[dst] = regs[src]
    elif op == 'STR':
        mem.append(ks[regs['R11'] // 12])
    else:
        raise Exception(op)

r0 = 0x5A
for m in reversed(mem):
    ch = r0 + 7 + m
    print(chr(ch), end='')
print()

