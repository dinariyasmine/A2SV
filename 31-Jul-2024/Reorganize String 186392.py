# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        h = []
        for char, freq in count.items():
            heapq.heappush(h, (-freq, char))
        
        res = []
        
        while len(h) >= 2:
            freq1, char1 = heapq.heappop(h)
            freq2, char2 = heapq.heappop(h)
            
            res.extend([char1, char2])
            #decrement the freq
            if freq1 + 1 < 0:
                heapq.heappush(h, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(h, (freq2 + 1, char2))
                
        if h:
            freq, char = heapq.heappop(h)
            #if we add just one of this char it's okay
            if -freq > 1:
                return ""
            res.append(char)
            
        return "".join(res)