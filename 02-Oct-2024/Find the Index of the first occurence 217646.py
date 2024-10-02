# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            ref = i
            for j in range(len(needle)):
                if haystack[ref] != needle[j]:
                    break
                ref += 1
            else:
                return i
                
        return -1