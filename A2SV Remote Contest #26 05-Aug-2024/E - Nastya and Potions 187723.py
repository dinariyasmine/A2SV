# Problem: E - Nastya and Potions - https://codeforces.com/gym/540348/problem/E

import sys
input = sys.stdin.readline
from collections import deque

def bfsTopoSort(graph, n):
    
    in_degree = [0] * n
    
    for node in range(n):
        for child in graph[node]:
            in_degree[child] += 1

    dq = deque([node for node in range(n) if in_degree[node] == 0])
    ans = []
    while dq:
        p = dq.popleft()
        ans.append(p)
        for child in graph[p]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                dq.append(child)

    return [] if len(ans) < n else ans

for _ in range(int(input())):
    n, k = map(int, input().split())
    potions = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    
    for i in tuple(map(int, input().split())):
        potions[i-1] = 0
        
    for i in range(n):
        for j in tuple(map(int, input().split()))[1:]:
            graph[i].append(j-1)
            
    order = bfsTopoSort(graph, n)
    order.reverse()
    for node in order:
        if len(graph[node]) > 0:
            potions[node] = min(potions[node], sum([potions[child] for child in graph[node]]))

    print(*potions)
