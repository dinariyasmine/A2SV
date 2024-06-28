# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dq = deque()
        direct = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        mx = float('inf')

        #we append all water cells
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dq.append((i,j,0))

        
        
        #we calculate the dist for each cell
        mx = 0
        while dq  :
            i,j,s = dq.popleft()
            mx = max(mx,s)
            for (d1,d2) in direct:
                i1, j1 = i + d1 , j + d2
                if 0 <= i1 < len(grid) and 0 <= j1 < len(grid[0]) and grid[i1][j1]==0 and (i1,j1) not in visited :
                    dq.append((i1,j1,s+1))
                    visited.add((i1,j1))
                    
        return mx if mx>0 else -1