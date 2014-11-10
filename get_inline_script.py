import re
import sys

filename = sys.argv[1]
inline = 0
with open(filename, 'r') as fp:
    for line in fp.readlines():
        if "inline script elements" in line and "No inline script" not in line:
            out = re.findall(r'\d+', line)
            if len(out) >= 2:
                inline = inline + int(out[1])

print "inline", inline
