import re
import sys

filename = sys.argv[1]
errors = int(0)
with open(filename, 'r') as fp:
    for line in fp.readlines():
        if "u'Invalid HTML" in line:
            out = re.findall(r'\d+ errors', line)
            if len(out) > 0:
                tmp = out[0].replace(' errors', '')
                errors = errors + int(tmp)

print "errors", errors
