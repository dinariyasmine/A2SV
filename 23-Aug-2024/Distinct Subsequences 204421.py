# Problem: Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for idx2 in range(n + 1):
            memo[m][idx2] = 1

        for idx1 in range(m - 1, -1, -1):
            for idx2 in range(n - 1, -1, -1):
                if t[idx1] == s[idx2]:
                    memo[idx1][idx2] = memo[idx1 + 1][idx2 + 1]+memo[idx1][idx2 + 1]
                else:
                    memo[idx1][idx2] = memo[idx1][idx2 + 1]

        return memo[0][0]
