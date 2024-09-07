# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        parent = []
        rank = []

        def initialize(size):
            nonlocal parent, rank
            parent = [i for i in range(size)]
            rank = [0] * size

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

        n = len(stones)
        initialize(n)
        

        for i in range(n):
            for j in range(n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1] :
                    union(i, j)
                    
        distinct = set(find(i) for i in range(n))
        return n - len(distinct)
        
            




        