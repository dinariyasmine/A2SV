# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        n = len(isWater)
        m = len(isWater[0])

        answer =[[-1 for _ in range(m)] for _ in range(n)]

        dq = deque()
        direct = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    dq.append((i,j))
                    answer[i][j]=0
                    visited.add((i,j))

        while dq and len(visited) != m*n:
            i,j = dq.popleft()
            mn = float('inf')
            for d1,d2 in direct:
                    i1,j1 = i+d1, j+d2
                    if 0 <= i1 < n and 0 <= j1 < m and (i1,j1) not in visited :
                        answer[i1][j1] = answer[i][j] + 1
                        visited.add((i1,j1))
                        dq.append((i1,j1))
        return answer


                

                    








        