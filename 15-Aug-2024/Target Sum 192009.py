# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(currentSum, idx):
            if idx == len(nums):
                return 1 if currentSum == target else 0

            if (currentSum, idx) in memo:
                return memo[(currentSum, idx)]
            memo[(currentSum, idx)] = dp(currentSum + nums[idx], idx + 1) + dp(currentSum - nums[idx], idx + 1)
            return memo[(currentSum, idx)]
            
        return dp(0,0)

        