# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        f = Counter(words)
        heap = [(-freq,word) for word,freq in f.items()]

        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
