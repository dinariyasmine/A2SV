# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        arr = set()
        for c in allowed:
            arr.add(c)
        cpt = len(words)
        for word in words:
            for c in word:
                if c not in allowed:
                    cpt -= 1
                    break
        return cpt

        