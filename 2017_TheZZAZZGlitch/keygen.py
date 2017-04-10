#!/usr/bin/env python3

"""
This was fun :)

(c) 2017 - kenoph
github.com/kenoph

LICENSE: MIT
"""

import functools
import operator


def s2b(xx):
    return [int("".join(x), 16) for x in zip(xx[::2], xx[1::2])]

flatten = lambda l: [item for sublist in l for item in sublist]

lookup = [0x67, 0x61, 0x64, 0x60, 0x69, 0x6B, 0x66, 0x65, 0x62, 0x6A, 0x63, 0x68, 0x6C, 0xF8, 0xFC, 0xFD]

ALPHABET = {
    0x60: 'A',
    0x61: 'B',
    0x62: 'C',
    0x63: 'D',
    0x64: 'E',
    0x65: 'F',
    0x66: 'G',
    0x67: 'H',
    0x68: 'I',
    0x69: 'V',
    0x6A: 'S',
    0x6B: 'L',
    0x6C: 'M',
    0xF6: '0',
    0xF7: '1',
    0xF8: '2',
    0xF9: '3',
    0xFA: '4',
    0xFB: '5',
    0xFC: '6',
    0xFD: '7',
    0xFE: '8',
    0xFF: '9',
}

KEY = s2b("""B46BCBDEB874E151593D66DDF3DA9D3F080AE6BB682179F1F2C369F5449FAA7762D12E008252BD5786763484643110FDADA9EA019A53E87B9B0D562250B161F794CE16D59091C7D8F93AC5368B7303AF3738A17A72C8B0024363D71D248525A846E4E033ACC0A76DF4950F4ED641B6991B2D788C97E9284FE36C1E9EB511CC877CA2478DEB708EA381FE4C5A8F5E4A5BEC1520D013FC92587E4B4905098830895FAB752680D2178A60AECFBE96555407ED0C9CCDBAA5322A2935128327EEC97F98E5B919C63E0E420BB71AA46A2CE2D3F8CA18F0DFDC231C3B48BCFBB265EF6EFADBF614716FD45D5C4D93FFD93945402FE76704C4B3A67DC22BC1BF1F063CA0
""")


def encode_helper(n):
    bc = 0x41A7
    hl = 0x72D4
    
    for i in range(n):
        hl = (hl + bc) & 0xFFFF
        
    return hl & 0xFF


def encode(flags, rnd, mins, secs):
    """
    Returns the password for the challenge.
    
    :param flags: the achievements bitfield
    :param rnd: a random value
    :param mins: number of minutes the game has been running
    :param secs: number of seconds the game has been running
    :returns: the password required to record the score
    """
    
    rnd &= 0xFE
    # flags &= 0x7F  # Commented out for the lulz
    out = [flags, rnd, mins, secs, 0, 0]
    key = [0x55, 0xAA, 0xF0, 0x0F]
    for i, k in enumerate(key):
        out[i] = KEY[out[i] ^ k]
    
    check_sum = (sum(out) + 0xC7) & 0xFF
    check_xor = (functools.reduce(operator.xor, out) ^ 0x8A) & 0xFF
    
    out[4] = encode_helper(check_sum)
    out[5] = encode_helper(check_xor)
    
    for i in range(4):
        out[i] ^= out[5]
    
    out_s = []
    for b in out:
        out_s.append(lookup[b & 0x0F])
        out_s.append(lookup[b >> 4])
    
    return "".join(map(ALPHABET.get, out_s))
    

# Actual maximum flag value is 0b01111111
print("PASS:", encode(0b11111111, 69, 0, 0))
