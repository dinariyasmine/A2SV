# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        print(n)
        visited = set()
        i, j = 0, 0

        for i in range(n):
            for j in range(n):
                to_move = matrix[i][j]
                while (i,j) not in visited:
                    print(matrix)
                    i1, j1 = j, n - i
                    print(i1,j1)
                    nxt = matrix[i1][j1]
                    matrix[i1][j1] = to_move
                    visited.add((i,j))
                    i, j = i1,j1
                    to_move = nxt
                else:
                    next
        
            
        