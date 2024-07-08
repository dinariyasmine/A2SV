# Problem: d - Valid BFS? - https://codeforces.com/gym/533316/problem/d


from collections import deque


def BFS(n,graph,trav):
    
    dq =deque([1])
    idx =1
    lg =len(trav)
    
    while dq:
        for _ in range(len(dq)):
            node =dq.popleft()
            numChild =len(graph[node])
            
            for i in range(numChild):
                if idx >=lg or trav[idx] not in graph[node]:
                    return "No"
                
                graph[node].remove(trav[idx])
                graph[trav[idx]].remove(node)
                dq.append(trav[idx])
                idx += 1
                
    return "Yes" if idx==lg and len(dq)==0 else "No"



def graph(n):
    graph =[set() for _ in range(n+1)]
    for u,v in [list(map(int, input().split(" ")))for _ in range(n - 1)]:
        graph[u].add(v)
        graph[v].add(u)
    return graph

n =int(input())
graph =graph(n)
trav =list(map(int, input().split(" ")))

print(BFS(n,graph,trav))
