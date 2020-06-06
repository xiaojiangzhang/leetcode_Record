import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
res = 1
for s in b:
    if s not in a:
        res = 0
sys.stdout.write(str(res))
