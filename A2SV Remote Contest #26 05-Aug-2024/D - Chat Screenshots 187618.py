# Problem: D - Chat Screenshots - https://codeforces.com/gym/540348/problem/D

from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    graph = defaultdict(list)
    prt = [0] * (n + 1)

    for _ in range(k):
        lst = list(map(int, input().split()))
        for i in range(1, len(lst) - 1):
            graph[lst[i]].append(lst[i + 1])
            prt[lst[i + 1]] += 1

    dq = deque()
    for i in range(1, n + 1):
        if prt[i] == 0:
            dq.append(i)

    answer = []
    while dq:
        node = dq.popleft()
        answer.append(node)
        for child in graph[node]:
            prt[child] -= 1
            if prt[child] == 0:
                dq.append(child)

    print('YES') if len(answer) == n else print('NO')
