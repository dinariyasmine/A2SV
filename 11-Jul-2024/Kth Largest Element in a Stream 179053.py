# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k =k
        self.h =[]
        for num in nums:
            self.add(num)

    def add(self,val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0] 
