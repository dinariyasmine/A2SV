# Problem: B - Guess the Maximum - https://codeforces.com/gym/535309/problem/B

t = int(input().strip())

res = []
for _ in range(t):
    n = int(input().strip())
    s = list(map(int,input().strip().split()))
    
    mini = max(s[0],s[1])
    
    for i in range(1, n - 1):
        mini = min(mini,max(s[i],s[i + 1]))
    
    res.append(str(mini-1))

print("\n".join(res))
