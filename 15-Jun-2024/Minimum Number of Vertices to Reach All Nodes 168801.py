# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        heads = set()
        trav = set()
        for edge in edges:
            
            src = edge[0]
            des = edge[1]
            heads.add(src)  
            trav.add(des)   
        output = [node for node in heads if node not in trav]
        return output



            

