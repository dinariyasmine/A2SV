# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(n - 2, -1, -1):
            for j in range(len(matrix[i])):
                memo = [matrix[i+1][j]]
                if j + 1 < m:
                    memo.append(matrix[i+1][j + 1])
                if j - 1 >= 0:
                    memo.append(matrix[i+1][j - 1])
                matrix[i][j] += min(memo)
        return min(matrix[0])



