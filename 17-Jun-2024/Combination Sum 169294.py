# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def btrac(idx,target,path):
            if target == 0:
                res.append(path)
                return
            if target<0:
                return 
            for i in range(idx,len(candidates)):
                btrac(i,target-candidates[i],path+[candidates[i]])
        candidates.sort()
        res = []
        btrac(0, target, [])
        return res
        