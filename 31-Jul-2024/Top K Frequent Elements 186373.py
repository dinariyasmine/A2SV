# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for c in count:
            heapq.heappush(heap,(-count[c],c))
        res = []
        for _ in range(k) :
            cnt, c = heapq.heappop(heap)
            res.append(c)
        return res
        
        