# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0

        for j in range(1, m):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = dp[j - 1][0]
            else:
                dp[j][0] = 0

        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = 0

        return dp[m - 1][n - 1]
        
        