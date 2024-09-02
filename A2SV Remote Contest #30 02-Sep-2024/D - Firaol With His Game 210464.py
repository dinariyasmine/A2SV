# Problem: D - Firaol With His Game - https://codeforces.com/gym/545837/problem/D

t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    cpt = 0
    maxi = 0
    max_idx = 0

    for i in range(n):
        cpt += a[i]
        
        if a[i] > maxi:
            maxi = a[i]
            max_idx = i + 1
        if cpt > s:
            print(max_idx)
            break
    else:
        print(0)