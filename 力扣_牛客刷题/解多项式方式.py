import numpy as np

a = eval(input())
b = eval(input())
print(a)
print(b)

a = np.array(a)
b = np.array(b)
x = np.linalg.solve(a, b)
x = list(x)
res = []
for i in range(len(x)):
    res.append(x[i])

print(res)
