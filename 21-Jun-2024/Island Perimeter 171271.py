# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:


        def dfs (i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            #already visited     
            if grid[i][j]==-5:
                return 0

            #mark as visited
            grid[i][j]=-5

            # we visit adjacent cases
            perim = dfs(i,j+1)
            perim+= dfs(i,j-1)
            perim+= dfs(i+1, j)
            perim+= dfs(i-1, j)
            return perim

        for i in range(len(grid)):
            curr = grid[i]
            for j in range(len(curr)):
                if grid[i][j]==1:
                    return dfs(i,j)
        return 0
                    



        