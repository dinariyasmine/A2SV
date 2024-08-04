# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [0] * len(edges)
        ans = -1
        for i in range(len(edges)):
            cpt = 1
            curr = i
            while curr >= 0:
                if visited[curr] != 0:
                    if visited[curr][0] == i:
                        ans = max(ans,cpt - visited[curr][1])
                    break
                else:
                    visited[curr] = [i,cpt]
                    cpt += 1
                    curr = edges[curr]
        return ans
