class UF():
    def __init__(self, n):
        # 图中的分量（子树）个数
        self.count = n
        # 记录每个节点的父节点 parent[i]表示第i个节点的父节点
        self.parent = [0 for i in range(n)]
        # size记录每个分量的大小，用于查找分量个数以及路径优化
        self.size = [0 for i in range(n)]
        for i in range(n):
            # 初始将每个分量的父节点标识为自己
            self.parent[i] = i
            self.size[i] = 1
        print(self.parent)

    def union(self, p, q):
        '''
        union用来连接合并pq两个分量
        :param p:
        :param q:
        :return:None
        '''
        rootP = self.parent[p]
        rootQ = self.parent[q]
        # 空间优化，将小树接到大树下，避免出现线性查找
        if self.size[p] > self.size[q]:
            self.parent[rootQ] = rootP
            # 更新当前分量中元素个数
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1

    def connected(self, p, q):
        # 查找两个分量是否连通
        return self.find(p) == self.find(q)

    def find(self, root):
        while self.parent[root] != root:
            # 进行路径压缩
            self.parent[root] = self.parent[self.parent[root]]
            root = self.parent[root]
        return root

    def count(self):
        return self.count


source = [[1, 2],
          [3, 4],
          [5, 6],
          [1, 6]]
uf = UF(7)
for data in source:
    # print(data)
    uf.union(data[0], data[1])
res = {}
for i in range(7):
    res[uf.find(i)] = res.get(uf.find(i), 0) + 1

print('parent', uf.parent)
print('size  ', uf.size)
print('res', max(res.values()))
