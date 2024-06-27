# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dq = deque()
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    dq.append((i,j))
                if grid[i][j]==1:
                    fresh += 1
        p = [(0,1),(0,-1),(1,0),(-1,0)]
        cpt = 0
        while dq and fresh :
            cpt +=1
            for r in range(len(dq)):
                x,y = dq.popleft()
                for (p1,p2) in p:
                    x1,y1 = x+p1 , y+p2
                    if 0 <= x1 < n and 0 <= y1 < m and grid[x1][y1] == 1:
                        grid[x1][y1]=2
                        fresh -= 1
                        dq.append((x1,y1))
        if fresh == 0:
            return cpt 
        else:
            return -1

