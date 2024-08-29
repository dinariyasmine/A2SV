# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxi = 1
        maxi_s = s[0]

        for i in range(len(s)-1):
            for j in range(i + 1, len(s)):
                # we check if it's a palindrom and if it's longer than the prev found
                if j - i + 1 > maxi and s[i:j+1] == s[i:j+1][::-1]:
                    maxi = j - i + 1
                    maxi_s = s[i:j+1]

        return maxi_s