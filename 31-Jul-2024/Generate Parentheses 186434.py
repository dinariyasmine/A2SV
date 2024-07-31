# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid_parentheses(s):
            stack = []
            for i in s:
                if i == '(':
                    stack.append(i)
                elif i == ')' and stack:
                    stack.pop()
                elif i == ')' and len(stack) == 0:
                    return False
                
            return len(stack) == 0
        
        res = []
        def btrack(s, n, l, res):
            
            
            
            if len(s) == l :
                if valid_parentheses(s):
                    res.append(s)
                    

                return s
            
            if n > 0:
                btrack(s+'(', n-1, l, res)
            
            btrack(s+')', n, l, res)

            


        btrack("(", n, 2 * n, res)
        return res

            




        




        