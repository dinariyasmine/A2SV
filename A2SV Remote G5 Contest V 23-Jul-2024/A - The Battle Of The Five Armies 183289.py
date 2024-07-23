# Problem: A - The Battle Of The Five Armies - https://codeforces.com/gym/508510/problem/A

cap = list(map(int, input().split()))
nbr = list(map(int, input().split()))

first = 0
for i in range(0,3):
    first += cap[i]*nbr[i]


second = 0

for i in range(3,5):
    second += cap[i]*nbr[i]

if first > second:
    print('WIN')
elif first < second:
    print('LOSE')
else:
    print('DRAW')