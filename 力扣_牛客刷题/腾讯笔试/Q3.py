"""

"""
import sys


def permute(nums, n):
    track = []
    res = []

    def backtrack(nums, track, n):
        if n == len(track):
            res.append(list(track))
            return
        for i in range(len(nums)):
            if len(track) == n:
                continue
            track.append(nums[i])
            backtrack(nums, track, n)
            track.pop()

    backtrack(nums, track, n)
    return res


m, n = sys.stdin.readline().strip().split(' ')
n = int(n)
m = int(m)

nums = [i for i in range(1, m+1)]
print(nums)
res = permute(nums, n)
print(len(res), res)
r = 0
for row in res:
    for j in range(n - 1):
        if row[j] == row[j + 1]:
            r += 1
            break

print(r % 10003)
