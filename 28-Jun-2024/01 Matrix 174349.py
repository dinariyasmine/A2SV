# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        n = len(mat)
        m = len(mat[0])

        dq = deque()
        direct = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        
        answer = [[float('inf') for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    dq.append((i, j))

        while dq :
            i,j= dq.popleft()
            s = answer[i][j]
            for (d1,d2) in direct:
                i1, j1 = i + d1 , j + d2
                if 0 <= i1 < len(mat) and 0 <= j1 < len(mat[0]):
                    if answer[i1][j1] > s + 1:
                        answer[i1][j1] = s + 1
                        dq.append((i1, j1))
                    
        return answer


                    

        