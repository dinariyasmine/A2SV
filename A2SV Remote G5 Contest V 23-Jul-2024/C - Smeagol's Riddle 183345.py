# Problem: C - Smeagol's Riddle - https://codeforces.com/gym/508510/problem/C

n = int(input())
for _ in range(n):
    s = input()

    cpt = 0
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            cpt += 1
    print(cpt)