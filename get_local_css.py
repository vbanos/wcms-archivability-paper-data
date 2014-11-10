import re
import sys

filename = sys.argv[1]
local = float(0)
remote = float(0)
with open(filename, 'r') as fp:
    for line in fp.readlines():
        if "Local CSS found:" in line:
            out = re.findall(r'\d+', line)
            if len(out) >= 3:
                local = local + float(out[1])
                remote = remote + float(out[2])

print "local", local, "remote", remote, "success", (local / (local + remote))
