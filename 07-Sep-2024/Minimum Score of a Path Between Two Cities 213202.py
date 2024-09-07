# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        parent = []
        rank = []

        def initialize(size):
            nonlocal parent, rank
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

        initialize(n)

        
        for road in roads:
            union(road[0] - 1, road[1] - 1)  

        root1 = find(0) 
        rootn = find(n - 1)  
        mini = float('inf')

        for i, j, w in roads:
            if find(i - 1) == root1:  
                mini = min(mini, w)

        return mini
