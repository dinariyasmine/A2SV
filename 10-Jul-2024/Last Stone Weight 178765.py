# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        answer = [-1 * i for i in stones]
        heapq.heapify(answer)
        while len(answer)>1:
            x = heapq.heappop(answer)
            y = heapq.heappop(answer)
            heapq.heappush(answer, -1*abs(x-y))
        return -1*answer[0]


        