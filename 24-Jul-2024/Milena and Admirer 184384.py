# Problem: Milena and Admirer - https://codeforces.com/problemset/problem/1898/B

import math
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    op = 0
    for i in range(n - 1, 0, -1):
        if a[i - 1] > a[i]:
            k = math.ceil(a[i - 1] / a[i])
            op += k - 1
            a[i - 1] = math.floor(a[i - 1] / k)

    print(op)
