# Problem: Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrome(s):
            return s == s[::-1]
        cpt = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if palindrome(s[i:j+1]):
                    cpt += 1
        return cpt