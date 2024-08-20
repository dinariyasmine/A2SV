# Problem: C - Hello World - https://codeforces.com/gym/543262/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    if arr[0] != 1:
        print('NO')
        continue
    arr.pop(0)
    cpt = 1
    for i in arr:
        if i > cpt:
            print('NO')
            break
        cpt += i
    else:
        print('YES')