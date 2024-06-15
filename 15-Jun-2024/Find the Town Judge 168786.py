# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        occ = {}
        occ_trst = {}
        
        for i in range(len(trust)):
            trst = trust[i]
            if trst[1] in occ:
                occ[trst[1]] +=1
            else:
                occ[trst[1]] = 1
            
            if trst[0] in occ_trst:
                occ_trst[trst[0]] += 1
            else:
                occ_trst[trst[0]] = 1
        
        for j in occ:
            if occ[j] == n - 1 and j not in occ_trst:
                return j
        
        if n < 2:
            return 1
        else:
            return -1

