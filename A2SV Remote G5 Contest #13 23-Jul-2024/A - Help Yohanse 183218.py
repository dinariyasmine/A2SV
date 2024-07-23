# Problem: A - Help Yohanse - https://codeforces.com/gym/521860/problem/A

n = int(input())

arr = list(range(1, n+1))

popped = arr.pop()
ans = [popped] +arr

print(*ans)
