# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def nice(sb):
            upper = set()
            lower = set()
            for char in sb:
                if char.islower():
                    lower.add(char)
                elif char.isupper():
                    upper.add(char.lower())
            return lower == upper
        
        n = len(s)
        lg = ""
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                sb = s[i:j]
                if nice(sb) and len(sb) > len(lg):
                    lg = sb
        return lg
