# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def initialize(size):
            global parent, rank
            parent = [i for i in range(size)]
            rank = [1] * size

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        def connected(x, y):
            return find(x) == find(y)

        n = len(isConnected)
        
        initialize(n)


        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        distinct = set(find(i) for i in range(n))
        return len(distinct)

        
        