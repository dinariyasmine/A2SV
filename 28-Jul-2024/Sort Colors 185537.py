# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        left = 0
        right = 0
        n = len(nums) 
        for left in range(n):
            right = left
            while right != n:
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                right += 1
        return nums


        
        

            
        