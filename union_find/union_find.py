# Algoritmo Union-Find

class UnionFind(object):
    def __init__(self, n):
        self.ID = [i for i in range(n)]

    def connected(self, p, q):
        return self.ID[p] == self.ID[q]

    def union(self, p, q):
        if not self.connected(p, q):
            pid = self.ID[p]
            qid = self.ID[q]
            for i in range(len(self.ID)):
                if self.ID[i] == pid:
                    self.ID[i] = qid

b = UnionFind(10)
b.union(4, 6)
b.union(8, 5)
print(b.ID)
