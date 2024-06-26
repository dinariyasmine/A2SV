# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cpt = 0
        def dfs(grid,i,j):
            #base case if we go outside grid or not land
            if i <0 or i >=len(grid) or j <0 or j >=len(grid[0]) or grid[i][j] =='0':
                return
            #we mark it as visited
            grid[i][j]='0'
            #we review all the 'connected' land
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    cpt += 1
                    dfs(grid,i,j)
        return cpt


        