# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        
        for curr in path.split('/'):
            if curr == '' or curr == '.':
                continue 
            elif curr == '..':
                if s:
                    s.pop()  
            else:
                s.append(curr)  

        res = '/' + '/'.join(s)
        return res
