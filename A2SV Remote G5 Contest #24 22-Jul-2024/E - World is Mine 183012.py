# Problem: E - World is Mine - https://codeforces.com/gym/536373/problem/E


import heapq
from typing import Counter

test = int(input())


for _ in range(test):
    n = int(input())
    lst = list(map(int, input().split()))
    
    cpt = Counter(lst)
    
    cakes = []
    
    for t in cpt:
        cakes.append((t,cpt[t]))
    
    cakes.sort()
    
    
    total_Bob = 0
    curr_Bob = []
    
    
    
    for i in range(len(cakes)):
        bob_turn = total_Bob+cakes[i][1]
        alice_turn = i-len(curr_Bob)
        total_Bob += cakes[i][1]
        heapq.heappush(curr_Bob, -cakes[i][1])
        if bob_turn> alice_turn:
            total_Bob += heapq.heappop(curr_Bob)
            
            
            
    print(len(cakes)-len(curr_Bob))
