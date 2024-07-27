# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        #i case input invalid
        if not matrix or not matrix[0]:
            return []
        
        n = len(matrix)
        m = len(matrix[0])
        up, down, left, right = 0, n-1, 0, m - 1
        res = []
        visited = set()

        while len(visited) != m*n:
            
            for j in range(left,right+1):


                if (up,j) not in visited:

                    res.append(matrix[up][j])
                    visited.add((up, j))
            up += 1

            for i in range(up,down+1):
                if (i,right) not in visited:
                    res.append(matrix[i][right])
                    visited.add((i,right))

            right -= 1

            if up<=down:
                for j in range(right, left-1,-1):
                    if (down,j) not in visited:
                        res.append(matrix[down][j])
                        visited.add((down,j))
                down -= 1

            if left <= right:
                for i in range(down,up-1,-1):
                    if (i,left) not in visited:
                        res.append(matrix[i][left])
                        visited.add((i,left))
                left += 1

        return res
