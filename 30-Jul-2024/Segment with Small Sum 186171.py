# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
a = list(map(int, input().split()))

    
left = 0
somme = 0
lgn = 0

for right in range(n):
    somme += a[right]

    while somme > s:
        somme -= a[left]
        left += 1

    lgn = max(lgn, right - left + 1)

print(lgn) 
