n, k = 5, 3
data = [[2, 11, 21],
        [19, 10, 1],
        [20, 11, 1],
        [6, 15, 24],
        [18, 27, 36]]
count = 0
visit = {(0, 0)}
for i in range(n):
    for j in range(n):
        if i == j or ((i, j) in visit and (j, i) in visit):
            continue
        visit.add((i, j))
        visit.add((j, i))
        res = False
        after = data[i][0] + data[j][0]
        for e in range(1, k):
            if data[i][e] + data[j][e] == after:
                res = True
            else:
                res = False
        if res:
            count += 1
            print(data[i], data[j], after)
print(visit)
print(count)
