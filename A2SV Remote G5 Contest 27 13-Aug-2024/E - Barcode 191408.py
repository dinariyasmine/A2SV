# Problem: E - Barcode - https://codeforces.com/gym/541399/problem/E


n, m, x, y = map(int, input().split())
board = [input() for _ in range(n)]

pref = [(0, 0)]
for i in range(m):
    dot = 0
    for j in range(n):
        if board[j][i] == '.':
            dot += 1
    pref.append((pref[-1][0] + n - dot, pref[-1][1] + dot))

dp = [[float('inf')] * 2 for _ in range(m + 1)]
dp[0][0] = dp[0][1] = 0

for i in range(1, m + 1):
    for j in range(2):
        for k in range(x, y + 1):
            if i - k < 0:
                continue
            cur = (pref[i][j] - pref[i - k][j]) + dp[i - k][1 ^ j]
            dp[i][j] = min(dp[i][j], cur)

print(min(dp[m][0], dp[m][1]))
