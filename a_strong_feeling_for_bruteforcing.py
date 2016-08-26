#!/usr/bin/env python3

import subprocess


def run(txt):
    return subprocess.run('./asf', input=txt, stdout=subprocess.PIPE).stdout


if __name__ == '__main__':
    key = b''
    
    for n in range(500):
        res = dict()
        for l in range(1, 128): 
            curr = key + bytes([l])
            out = run(curr)
            if out not in res:
                res[out] = curr
            else:
                del res[out]
        
        key = list(res.values())[0]
        if key[-1] == 0x7F:
            key = key[:-1]
            break
    
    print(key)
