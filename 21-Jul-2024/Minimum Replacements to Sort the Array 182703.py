# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        def is_sorted(nums):
            return nums == sorted(nums)

        if is_sorted(nums):
            return 0

        n = len(nums) - 2
        final = nums[len(nums)-1]
        cpt = 0

        while n  >= 0:
            if nums[n] > final:
                curr = nums[n] // final
                if nums[n] % final :
                    curr += 1 
                final = nums[n] // curr
                cpt += curr - 1
            else:
                final = nums[n]
            n -= 1
        return int(cpt)


        