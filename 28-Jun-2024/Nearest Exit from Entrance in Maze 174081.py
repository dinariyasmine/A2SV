# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def is_exit(i,j):
            if 0 <= i < len(maze) and 0 <= j < len(maze[0]):
                if [i,j] != entrance:
                    if maze[i][j]=='.':
                        if i == 0 or i == len(maze) -1 or j == 0 or j ==len(maze[0]) - 1:
                            return True
            return False

        dq = deque([(entrance[0],entrance[1],0)])
        direct = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set((entrance[0],entrance[1]))
        steps = 0
        while dq :
            steps += 1
            i, j , steps = dq.popleft()
            for (d1,d2) in direct:
                i1, j1 = i + d1 , j + d2
                if is_exit(i1,j1):
                    return steps + 1
                else:
                    if 0 <= i1 < len(maze) and 0 <= j1 < len(maze[0]) and maze[i1][j1] == '.' and (i1,j1) not in visited:
                        visited.add((i1,j1))
                        
                        dq.append((i1,j1,steps+1))
        return -1









        


        