# Problem: C - The Lakes - https://codeforces.com/gym/535309/problem/C

from collections import deque

t =int(input())
for _ in range(t):
    n,m =map(int,input().split())
    lake= []
    for _ in range(n):
        lake.append(list(map(int,input().split())))

    def bfs(x,y):
        dq = deque([(x,y)])
        visited.add((x,y))
        answer= lake[x][y]

        while dq:
            i, j = dq.popleft()
            for d1, d2 in [(0,1),(0,-1),(1,0),(-1,0)]:
                i1, j1 = i + d1, j + d2
                if 0 <= i1 < n and 0 <= j1 < m and lake[i1][j1] > 0 and (i1,j1) not in visited:
                    visited.add((i1,j1))
                    answer += lake[i1][j1]
                    dq.append((i1,j1))
        return answer

    answer = 0
    visited = set()

    for i in range(n):
        for j in range(m):
            if lake[i][j]> 0 and (i,j) not in visited:
                answer = max(answer,bfs(i,j))

    print(answer)
