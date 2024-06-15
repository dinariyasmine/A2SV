# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        stack = []
        def btrac(idx=0):
            if idx == n:
                return len(stack)>1

            for i in range(idx + 1,n + 1):
                nbr = int(s[idx:i])
                if stack and stack[-1] != nbr+1:
                    continue
                stack.append(nbr)
                if btrac(i):
                    return True
                stack.pop()
            return False
                
        return btrac(0)
        




        