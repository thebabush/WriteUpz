#!/usr/bin/env python3

import json


# The trace data
data = json.load(open('calc.trace_15993a223f9b4a3799251447a8f8198f1ff787ed', 'r'))

# Base address of the trace
base = int(data[0]['base_addr'], 16)

# Output files
trace = open('trace.txt', 'w')
formula = open('formula.txt', 'w')


# Print and save to file
def pp(what):
    print(what, end='')
    formula.write(what)


for l in data[4:-1]:
    # Rebase the trace
    addr    = int(l['inst_addr'], 16) - base
    taken   = l['branch_taken']

    # Write rebased branch address
    trace.write(f'{addr:04X}\n')

    # This could have been a map, but I didn't know when starting :)
    if addr == 0xE87:
        if not taken:
            break
    elif addr == 0xBE9:
        if not taken:
            pp(',')
    elif addr == 0xC22:
        if not taken:
            pp('X')
    elif addr == 0xC58:
        if not taken:
            pp('+')
    elif addr == 0xCAF:
        if not taken:
            pp('-')
    elif addr == 0xD06:
        if not taken:
            pp('*')
    elif addr == 0xD5D:
        if not taken:
            pp('m')
    elif addr == 0xDB4:
        if not taken:
            pp('M')
    elif addr == 0xE08:
        if not taken:
            pp('C')

# End the file with a new line
pp('\n')

# Close the output files
formula.close()
trace.close()

