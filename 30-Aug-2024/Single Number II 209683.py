# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums):
        count = defaultdict(int)
        
        for i in nums:
            count[i] += 1

        for i, fq in count.items():
            if fq == 1:
                return i
        
        return -1