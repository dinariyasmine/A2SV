# Problem: D - Firaol And His Weapon - https://codeforces.com/gym/541399/problem/D

from collections import Counter

n = int(input())
planets = list(map(int, input().split()))
c = Counter(planets)
max_mass = max(planets)
dp = [0] * (max_mass + 1)
take = [0] * (max_mass + 1)

dp[1] = c[1]

take[1] = c[1]

for i in range(2, max_mass + 1):
    take[i] =  dp[i-2] + i* c[i]
    dp[i] = max(dp[i-1], take[i])


print(dp[max_mass])
