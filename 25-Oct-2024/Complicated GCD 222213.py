# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

a, b = map(int, input().split())

if a == b:
    print(a)
elif b - a == 1:
    print(1)
elif b - a > 1:
    print(1)