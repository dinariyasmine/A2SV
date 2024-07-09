# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        m = [-pile for pile in piles]
        heapq.heapify(m)
        
        
        for _ in range(k):
            
            n = -heapq.heappop(m)
            h = n - n // 2
            heapq.heappush(m, -h)
        
        
        somme = -sum(m)
        return somme
