# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n 
        ways = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        ways[i] = ways[j] 
                    elif dp[j] + 1 == dp[i]:
                        ways[i] += ways[j]
        
        maxi = max(dp)
        return sum(ways[i] for i in range(n) if dp[i] == maxi)
