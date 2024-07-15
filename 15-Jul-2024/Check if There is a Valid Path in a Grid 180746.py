# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        
        


        def can_connect(i, j, i1, j1):
            start = grid[i][j]
            target = grid[i1][j1]

            direct = {
                
                1: [(0, -1), (0, 1)],   # Left, Right
                2: [(-1, 0), (1, 0)],   # Up, Down
                3: [(0, -1), (1, 0)],   # Left, Down
                4: [(0, 1), (1, 0)],    # Right, Down
                5: [(0, -1), (-1, 0)],  # Left, Up
                6: [(0, 1), (-1, 0)]    # Right, Up
            }

            
            d = (i1 - i, j1 - j)
            if d not in direct[start]:
                return False
            opposited = (-d[0], -d[1])
            return opposited in direct[target]



        n = len(grid)
        m = len(grid[0])
        
        visited = set()
        dq = deque([(0,0)])
        visited.add((0,0))
        direct = [(0,1),(0,-1),(1,0),(-1,0)]
        cpt = 1
        while dq:
            i, j = dq.popleft()
            
            for d1, d2 in direct:
                i1, j1 = i + d1, j + d2
                if 0 <= i1 < n and 0 <= j1 < m and (i1,j1) not in visited :
                    
                    if can_connect(i,j,i1,j1):
                        dq.append((i1,j1))
                        
                        visited.add((i1,j1))
        print(visited)
        return (n - 1, m - 1) in visited
        

        
        