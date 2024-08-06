# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def helper(i):
            if i == 0 or i == 1:
                return i
            if memo[i] == -1:
                memo[i] = helper(i-1) + helper(i-2)
            return memo[i]
        return helper(n)
        