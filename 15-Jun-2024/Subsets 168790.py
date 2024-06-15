# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def btrac(start: int, path: List[int]):
            res.append(path[:])  
            for i in range(start, len(nums)):
                path.append(nums[i])
                btrac(i+1, path)
                path.pop()
        btrac(0, [])
        return res