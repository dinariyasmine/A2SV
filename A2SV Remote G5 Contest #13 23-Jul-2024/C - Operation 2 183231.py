# Problem: C - Operation 2 - https://codeforces.com/gym/521860/problem/C

from collections import deque

def bfs(a,b):
    if a == b:
        return 0
    
    dq = deque([(a, 0)])
    visited = set()  
    
    while dq:
        curr, op = dq.popleft()
        mul = curr * 2
        sub = curr - 1
        
        if mul == b or sub == b:
            return op + 1
        
        
        if mul not in visited and mul <= 2*b:  
            visited.add(mul)
            dq.append((mul, op+1))
        
        if sub not in visited and sub > 0:
            visited.add(sub)
            dq.append((sub, op+1))
    
    return -1  


a,b = map(int, input().split())

print(bfs(a,b))
