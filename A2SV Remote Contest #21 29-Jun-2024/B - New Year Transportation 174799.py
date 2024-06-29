# Problem: B - New Year Transportation - https://codeforces.com/gym/532332/problem/B

n,t = map(int, input().split())
a = list(map(int, input().split()))

#changed to iterative maybe recusion was too deep
curr = 1 

while curr < t:
    
    curr =curr +a[curr-1]
    if curr == t:
        print("YES")
        break
else:
    
    
    print("NO")
