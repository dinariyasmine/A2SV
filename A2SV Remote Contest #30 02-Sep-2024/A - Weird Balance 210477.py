# Problem: A - Weird Balance - https://codeforces.com/gym/545837/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a.count(a[0]) == len(a):
        print('NO')
        continue
        
    a.sort(reverse=True)
    
    if a[0] == a[1]:
        a[1], a[n - 1] = a[n - 1], a[1]
    print('YES')
    print(*a)