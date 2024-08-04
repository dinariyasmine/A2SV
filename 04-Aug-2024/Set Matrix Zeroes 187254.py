# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros_idx = set()
        for i in range(len(matrix)):
            for j in range((len(matrix[0]))):
                if matrix[i][j] == 0 :
                    zeros_idx.add((i,j))
        

        for (i,j) in zeros_idx:

            for m in range(len(matrix[i])):
                matrix[i][m] = 0

            for n in range(len(matrix)):
                matrix[n][j] = 0
        

        
        