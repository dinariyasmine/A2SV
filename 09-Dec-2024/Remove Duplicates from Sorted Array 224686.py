# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cpt = 1
        idx = 1
            
        for i in range(1, len(nums)):
            
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1
                cpt += 1

        return cpt
            
        