# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor = 0
      
        if len(nums1) % 2 != 0:
            for i in nums2:
                xor ^= i

        
        if len(nums2) % 2 != 0:
            for i in nums1:
                xor ^= i
        return xor
        
        