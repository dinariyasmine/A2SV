# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import deque
n,m= map(int, input().split())
a,b= map(int, input().split())
edges =[]

for i in range(m):
    
    edges.append(tuple(map(int, input().split())))


#we contruct the graoh 
graph = [[] for _ in range(n + 1)]
for u,v in edges  :    
    graph[u].append(v)
    graph[v].append(u)


dq= deque([a])
dist= [-1]*(n + 1)
prnt= [-1]*(n + 1)
dist[a] = 0

#bfs
while dq:
    curr= dq.popleft()


    for ngh in graph[curr]:

        if dist[ngh]== -1:
            dq.append(ngh)
            dist[ngh] =dist[curr] + 1
            prnt[ngh] =curr

            if ngh==b:
                break

if dist[b]==-1:
    print(-1)


else:
    path= []
    curr= b

    while curr!=-1:
        path.append(curr)
        curr= prnt[curr]

    path.reverse()
    


    print(dist[b])
    print(" ".join(map(str, path)))