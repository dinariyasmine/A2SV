# Problem: A - Forever Winter - https://codeforces.com/gym/532332/problem/A

import collections
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    adj_lst = {i: [] for i in range(1, n + 1)}
    # n => nbr of nodes
    # m => nbr of edges
    for _ in range(m):
        u, v = map(int,input().split())
        adj_lst[u].append(v)
        adj_lst[v].append(u)
    
    leafs = set()
    for i in range(1,n+1):
        if len(adj_lst[i])==1:
            leafs.add(i)
            
            
        
    nbr_leafs = len(leafs)
    
    
    
    x = n - nbr_leafs - 1
    
    y = nbr_leafs // x
    
    print(x,y)
    
        
    
    
