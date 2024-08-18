# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        
        for i in s:

            if i.isalnum() == False:
                s = s.replace(i, "")

        return s == s[::-1]