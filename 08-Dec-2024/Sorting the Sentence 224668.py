# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        ans = {}
        currL = ''
        currPos = ''
        i = 0
        while i < (len(s)):
            if s[i].isalpha():
                currL += s[i]
            if s[i].isdigit():
                currPos += s[i]
            if i == len(s) - 1 or s[i + 1] == ' ':
                ans[int(currPos)] = currL
                currL = ''
                currPos = ''
            i += 1

        res = ' '.join(ans[i] for i in range(1, len(ans) + 1)) 
        return res





             


            
        