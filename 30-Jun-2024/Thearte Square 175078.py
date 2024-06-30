# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import math



def minF(n,m,a):
    L= (n+a-1) //a
    W= (m+a-1)// a
    return L*W
n,m,a = map(int, input().split())
print(minF(n, m, a))