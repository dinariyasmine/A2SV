# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        curr = ''
        arr = []
        for c in s:
            if ord(c) != 32:
                curr += c
            else:
                arr.append((curr[:len(curr) - 1] , curr[-1]))
                curr = ''
        if curr:
            arr.append((curr[:len(curr) - 1] , curr[-1]))
        return ''.join(x[0] + ' ' for x in sorted(arr, key=lambda x: int(x[1]))).strip()
