class UnionFind():
    def __init__(self, n):
        self.count = n
        self.parent = [0 for _ in range(n)]
        self.size = [0 for _ in range(n)]
        # 将不同分量的父节点初始化为自己
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def union(self, p, q):
        root_p = self.parent[p]
        root_q = self.parent[q]
        if self.size[p] > self.size[q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        self.count -= 1

    def find(self, root):
        while self.parent[root] != root:
            self.parent[root] = self.parent[self.parent[root]]
            root = self.parent[root]
        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)
