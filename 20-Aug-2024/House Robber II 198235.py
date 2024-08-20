# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        memo = [0] * n
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        mem = [0] * n
        mem[n - 1] = nums[n - 1]
        mem[n - 2] = max(nums[n - 1], nums[n - 2])

        #exclude the last one
        for i in range(2, n - 1):
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])
        
        #exclude the first one
        for i in range(n - 3, 0, -1):
            mem[i] = max(mem[i + 1], nums[i] + mem[i + 2])
    
        return max(memo[n - 2], mem[1])
        