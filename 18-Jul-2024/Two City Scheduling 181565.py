# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key= lambda x: -abs(x[0]-x[1]))
        total = 0
        A = 0
        B = 0
        n = len(costs) //2

        for xa,xb in costs:
            if (xa <= xb and A < n) or (B == n):
                total += xa
                A += 1
            else:
                total += xb
                B += 1
        
        return total

