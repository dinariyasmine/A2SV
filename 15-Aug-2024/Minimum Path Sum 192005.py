# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]

        

        for i in range(n):
            for j in range(m):
                print(i, j)
                if i == 0 and j == 0:
                    dp [i][j] = grid[0][0]
                else:
                    left, upper = inf, inf
                    if j - 1 >= 0:
                        left = dp[i][j - 1]
                    if i - 1 >= 0:
                        upper = dp[i - 1][j]
                    print(left, upper)
                    dp[i][j] = min(left, upper) + grid[i][j]
        return dp[n - 1][m - 1]
        