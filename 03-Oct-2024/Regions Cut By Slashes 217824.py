# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
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


        n = len(grid)
        ans = n * n * 4  
        initialize(ans)

        for i in range(n):
            for j in range(n):
                idx = i * n + j
                if i < n - 1:
                    # bottom union upper
                    union(4 * idx + 2, 4 * (idx + n))
                if j < n - 1:
                    # right union left
                    union(4 * idx + 1, 4 * (idx + 1) + 3)
                if grid[i][j] == '/':
                    union(4 * idx, 4 * idx + 3)
                    union(4 * idx + 1, 4 * idx + 2)
                elif grid[i][j] == '\\':
                    union(4 * idx, 4 * idx + 1)
                    union(4 * idx + 2, 4 * idx + 3)
                else:
                    union(4 * idx, 4 * idx + 1)
                    union(4 * idx + 1, 4 * idx + 2)
                    union(4 * idx + 2, 4 * idx + 3)

        distinct = set(find(i) for i in range(ans))
        return len(distinct)