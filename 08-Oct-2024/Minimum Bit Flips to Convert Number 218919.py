# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xoor = start ^ goal
        ans = 0
        while xoor > 0:
            ans += xoor & 1  
            xoor >>= 1     
        
        return ans
        