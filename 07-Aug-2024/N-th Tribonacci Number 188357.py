# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def helper(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if memo[i] == -1:
                memo[i] = helper(i-1) + helper(i-2) + helper(i-3)
            return memo[i]
        return helper(n)
        