# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        b = len(costs) - 1
        h1, h2 = [], []
        i = 0
        c = 0
        while k > 0:
            while len(h1) < candidates and i <= b:
                heapq.heappush(h1,costs[i])
                i += 1
            while len(h2) < candidates and i <= b:
                heapq.heappush(h2,costs[b])
                b -= 1
            cd1 = h1[0] if h1 else float('inf')
            cd2 = h2[0] if h2 else float('inf')
        
            if cd1 <= cd2:
                c += cd1
                heapq.heappop(h1)
            else:
                c += cd2
                heapq.heappop(h2)
            k -= 1
        return c