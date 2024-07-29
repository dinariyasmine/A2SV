# Problem: B - Chef Jamie - https://codeforces.com/gym/537575/problem/B

n = int(input())
fruits = list(map(int, input().split()))
fruits_sorted = sorted(fruits)


cpt = 0

for i in range(n):
    cpt += fruits[i] != fruits_sorted[i]
        
sw = max(0,cpt - 1)
        
print(sw)

