# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
       
        n = len(nums)
        for i in range(n):
            
            if i != sorted_nums[i]:
                return i
        return n
        