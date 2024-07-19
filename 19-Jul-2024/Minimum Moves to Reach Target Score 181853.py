# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cpt = target 
        curr = 1
        op = 0
        while cpt != 1:
            if maxDoubles != 0 and cpt % 2 == 0 :
                cpt = cpt // 2
                op += 1
                maxDoubles -= 1
            elif maxDoubles == 0:
                op += cpt - 1
                cpt = 1
            else:
                cpt -= 1
                op += 1
        return op
        