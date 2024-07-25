# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direct = [(0,1),(0,-1),(1,0),(-1,0)]
        n = len(board)
        m = len(board[0])
        visited = set()

        def btrack(i,j,l):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[l] or (i, j) in visited:
                return False
            if l == len(word)- 1:
                return True
            visited.add((i,j))
            for d1, d2 in direct:
                i1, j1 = i + d1, j + d2
                if btrack(i + d1, j + d2, l + 1):
                    return True
            visited.remove((i, j))
            return False
                    
            



        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if btrack(i,j,0) :
                        return True
        return False
                    
        
