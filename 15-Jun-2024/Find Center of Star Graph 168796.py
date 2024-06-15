# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        p = edges[0][0]
        q = edges[0][1]
       
       
        for edge in edges:
            if p in edge and q in edge:
                continue
            if p and p in edge:
                q = None
            if q and q in edge:
                p = None
        if p : 
            return p
        else:
            return q
                


        