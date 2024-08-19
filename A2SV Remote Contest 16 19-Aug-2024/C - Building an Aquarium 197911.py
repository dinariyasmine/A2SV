# Problem: C - Building an Aquarium - https://codeforces.com/gym/525787/problem/C

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    mini = 0
    maxi = max(a) + x
    
    
    while mini < maxi:
        mid = mini + (maxi - mini + 1) // 2
        curr = 0
        
        for i in range(n):
            curr += max(mid - a[i], 0)
            
        if curr <= x:
            mini = mid
        else:
            maxi = mid - 1
    
    print(mini)
