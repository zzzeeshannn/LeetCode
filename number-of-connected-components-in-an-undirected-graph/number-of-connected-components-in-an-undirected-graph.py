class Solution:
    def init(self, size):
        self.root = [i for i in range(size)]
        self.count = size
        self.rank = [1] * size
        
    def find(self, x):
        if x == self.root[x]:
            return x 
        else:
            self.root[x] = self.find(self.root[x])
        
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
    
    def components(self):
        return self.count 
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.init(n)
        for i in range(len(edges)):
            self.union(edges[i][0], edges[i][1])
        
        return self.components()