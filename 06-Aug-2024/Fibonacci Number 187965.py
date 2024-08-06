# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        @cache
        def helper(i):
            if i == 0 or i == 1:
                return i
            return helper(i - 1) + helper(i - 2)
        
        return helper(n)
