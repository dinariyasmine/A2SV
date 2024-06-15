# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        def cnx(node: int) -> int:
            cpt = 0
            
            for road in roads:
                if road[0] == node or road[1] == node:
                    cpt += 1
            return cpt
        dic = {}
        for i in range(n):
            dic[i] = cnx(i)
        maxi = 0
        for i in range(n):
            for j in range(i + 1, n):
                rnk = dic[i] + dic[j]
                if any((road[0] == i and road[1] == j) or (road[0] == j and road[1] == i) for road in roads):
                    rnk -= 1
                maxi = max(maxi, rnk)
        return maxi
