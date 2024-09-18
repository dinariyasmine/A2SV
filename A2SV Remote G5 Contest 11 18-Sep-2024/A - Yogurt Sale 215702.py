# Problem: A - Yogurt Sale - https://codeforces.com/gym/518838/problem/A

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    
    if ((n // 2) * b)  + ((n % 2) * a) < n * a:
        print(((n // 2) * b)  + ((n % 2) * a))
    else:
        print(n * a)