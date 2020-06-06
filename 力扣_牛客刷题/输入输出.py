import sys

# 单行字符型输入
input_sigle_line = sys.stdin.readline().strip()
print(input)
# 多行字符型输入
re = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    temp = list(map(int, line.split(' ')))
    re.append(temp)
print(re)
input = sys.stdin.readline().strip()
input = list(map(int, input.split(' ')))
print(input)
res = []
for i in range(0, len(input), 3):
    temp = []
    for j in range(i, i + 3):
        temp.append(input[j])
    res.append(temp)
print(res)
