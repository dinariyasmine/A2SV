# Problem:  King Escape - https://codeforces.com/problemset/problem/1033/A

a = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

ssx = (bx < ax) == (cx < ax)
ssy = (by < ay) == (cy < ay)

if ssx and ssy:
    print("YES")
else:
    
    print("NO")