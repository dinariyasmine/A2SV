# Problem: C - Tournament - https://codeforces.com/gym/544347/problem/C

from math import floor

def max_points(n, k, produce):
    dp = [[0] * 14 for _ in range(n+1)]

    for i in range(n - 1, -1, -1):
        for x in range(14):
            
            curr = produce[i] // (2 ** x)
            full = curr - k + dp[i + 1][x]
            
            if x + 1 < 14:
                half = floor(curr / 2) + dp[i + 1][x + 1]
            else:
                half = 0  



            dp[i][x] = max(full, half)

    return dp[0][0]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    produce = list(map(int, input().split()))
    print(max_points(n, k, produce))
