# 运动会
import sys


def get_half(start, end):
    num = end - start
    return int(num / 2) + 1


N = input()
project = []
while True:
    line = sys.stdin.readline().strip()
    if line:
        temp = list(map(int, line.split(' ')))
        project.append(temp)
    else:
        break
project.sort()
flag = -1
current_time = 0
for i in range(len(project)):
    start = project[i][0]
    end = project[i][1]
    stay_time = get_half(start, end)
    current_time = start + stay_time
    # for j in range(i,len(project)):
    #     if
