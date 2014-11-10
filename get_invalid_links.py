import re
import sys

filename = sys.argv[1]
correct = float(0)
invalid = float(0)
with open(filename, 'r') as fp:
    for line in fp.readlines():
        if "u'Links'" in line:
            out = re.findall(r'\d+', line)
            if len(out) > 3:
                correct = correct + float(out[1])
                invalid = invalid + float(out[2])

print "correct", correct, "invalid", invalid, "success", (correct / (correct + invalid))
