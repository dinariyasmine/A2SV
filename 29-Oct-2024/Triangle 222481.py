# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        dp = [[(float(inf))] * len(triangle[n - 1]) for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(n):
                if i == j:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        res = float('inf')
        for i in range(n):
            for j in range(n):
                if i < j and j - 1 >= 0 :
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1]) + triangle[j][i]
                    
        for i in range(n):
            for j in range(n):
                if j == n - 1:
                        res = min(res, dp[i][j])

        return res



                
        




        