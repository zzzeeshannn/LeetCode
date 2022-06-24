class Solution:
    def init(self, size):
            self.root = [i for i in range(size)]
            self.rank = [1]*size
            self.size = size
            
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
        
    def provinces(self):
            return len(set([self.find(i) for i in range(self.size)]))
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected[0])
        self.init(size)
        for i in range(size):
            for j in range(size):
                if isConnected[i][j] == 1:
                    self.union(i, j)
        
        return self.provinces()