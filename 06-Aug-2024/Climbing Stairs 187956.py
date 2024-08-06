# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:

    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(i):
            if i == 1:
                return 1
            elif i == 2:
                return 2

            if i not in memo:
                memo[i] = helper(i-1) + helper(i-2)

            return memo[i]
        return helper(n)