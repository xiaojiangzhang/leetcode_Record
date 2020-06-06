import collections


def plus_one(node, j):
    # print(node)
    x = int(node[j])
    if x == 9:
        y = 0
    else:
        y = x + 1
    # print(node[:j] + str(y) + node[j + 1:])
    return node[:j] + str(y) + node[j + 1:]


def down_one(node, j):
    x = int(node[j])
    if x == 0:
        y = 9
    else:
        y = x - 1
    return node[:j] + str(y) + node[j + 1:]


def Find(deadends, target):
    q = ['0000']
    visit = ['0000']
    step = 0
    while q:
        for i in range(len(q)):
            cur = q[0]
            q = q[1:]

            if cur in deadends:
                continue
            if cur == target:
                return step
            for j in range(4):
                up = plus_one(cur, j)
                down = down_one(cur, j)
                # print(up,j)
                # print(down,j)
                if up not in visit:
                    q.append(up)
                    visit.append(up)
                if down not in visit:
                    q.append(down)
                    visit.append(down)
        step += 1
    return -1


# 优化，双向BFS
def Find2(deadends, target):
    # q1从上往下遍历
    q1 = {'0000'}
    # visit记录遍历过的节点
    visit = {'0000'}
    # q2从下往上遍历
    q2 = {target}
    step = 0
    while q1 and q2:
        temp = set()
        # 扩散q1中的所有节点
        for cur in q1:
            if cur in deadends:
                continue
            if cur in q2:
                return step
            visit.add(cur)
            for j in range(4):
                up = plus_one(cur, j)
                down = down_one(cur, j)
                if up not in visit:
                    temp.add(up)
                if down not in visit:
                    temp.add(down)
        print(temp)
        step += 1
        q1 = q2
        q2 = temp
    return -1


# {'', '0100', '9000', '0001', '0900', '0010', '0009', '1000', '0090'}
# {'', '0302', '0292', '1202', '9202', '0203', '0102', '0212', '0201'}

res = Find2(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202")
print(res)
