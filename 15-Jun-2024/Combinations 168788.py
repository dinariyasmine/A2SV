# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def btrac(start: int, path: List[int]):
            if len(path) == k:
                #to append a copy of the curr path
                res.append(path[:])
                return
            for i in range(start, n + 1):
                #we append 
                path.append(i)
                #we check if we can append more to this path
                btrac(i + 1, path)
                #if we can't we pop the last element that caused k =len(path)
                path.pop()

        btrac(1, [])
        return res
