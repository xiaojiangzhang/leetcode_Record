import sys

num = int(sys.stdin.readline().strip())
count = 1
test = []
while count <= num:
    line = sys.stdin.readline().strip()
    if not line:
        break
    test.append(int(line))
    count += 1


def nums(n):
    if n <= 1:
        return n
    res = 0
    pre = 1
    for i in range(2, n + 1):
        res = res + pre
        pre = res

    return res


for t in test:
    sys.stdout.write(str(nums(t)) + '\n')
