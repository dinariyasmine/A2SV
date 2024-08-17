# Problem: C - Collecting Game - https://codeforces.com/gym/541399/problem/C


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    a = sorted(arr, reverse = True)
    
    sf = a.copy()
    
    for i in range(n - 2, -1, -1):
        sf[i] += sf[i + 1]
        
    ans = [0] * n
    ans[0] = n - 1
    
    for i in range(1, n):
        ans[i] = n - 1 - i
        if sf[i] >= a[i - 1]:
            ans[i] = ans[i - 1]
    ans_dic = dict.fromkeys(a, 0)
    for i in range(n):
        ans_dic[a[i]] = ans[i]
    for x in arr:
        print(ans_dic[x], end = ' ')
    print()