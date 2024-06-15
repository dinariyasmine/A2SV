# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def btrac(curr,used):
            if len(curr)==len(nums):
                res.append(curr[:])
                return
                
            for i in range(len(nums)):
                if not used[i]:
                    curr.append(nums[i])
                    used[i]=True
                    btrac(curr,used)
                    curr.pop()
                    used[i] = False
        res =[]
        used = [False] * len(nums)
        btrac([], used)
        return res