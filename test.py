import sys
import re

homes = input().split()
for line in sys.stdin:
    print(line.rstrip())
    match = re.search('swap ([a-z][0-9]) and ([a-z][0-9])', line, re.I)
    if not match:
        continue
    idx1 = homes.index(match.group(1))
    idx2 = homes.index(match.group(2))
    homes[idx1], homes[idx2] = homes[idx2], homes[idx1]

sorted_homes = sorted(homes)
print(' '.join(homes))
print(' '.join(sorted_homes))
if homes == sorted_homes:
    print('Nice')
else:
    print('Nooooooooo')
