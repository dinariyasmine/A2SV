# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        s = str(num)
        n = len(s)
        stack = []
        def btrac(idx=0):
            if idx == n:
                return len(stack) > 2

            for i in range(idx + 1, n + 1):
                nb = s[idx:i]
                if nb[0] == '0' and len(nb) > 1:
                    continue
                nbr = int(nb)
                if len(stack) >= 2 and stack[-1] + stack[-2] != nbr:
                    continue
                stack.append(nbr)
                if btrac(i):
                    return True
                stack.pop()
            return False
                
        return btrac(0)
