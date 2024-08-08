# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        n = len(nums)
        memo = {}
        def helper(idx, currSum):
            if idx >= n or currSum > target:
                return False
            if currSum == target:
                return True
            if (idx, currSum) not in memo:
                memo[(idx, currSum)] = helper(idx + 1, currSum + nums[idx]) or helper(idx + 1, currSum)
            return memo[(idx, currSum)] 
        
        return helper(0, 0)