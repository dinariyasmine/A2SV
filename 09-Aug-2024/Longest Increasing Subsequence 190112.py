# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        n = len(nums)
        memo = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)

        return max(memo)