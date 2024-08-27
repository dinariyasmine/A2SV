# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            inter = i  
            cpt = 0
            while inter > 0:
                cpt += inter % 2
                inter = inter // 2
            ans.append(cpt)
        return ans