# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

def AddEdge(u,v,adjLst):
    adjLst[u].append(v)
    adjLst[v].append(u)
    return adjLst
def Vertex(u,adjLst):
    if adjLst[u]:
        
        output = " ".join(map(str, adjLst[u]))
        print(output)
n = int(input())
k = int(input())
adjLst = {i: [] for i in range(1, n + 1)}
operations = []
for _ in range(k):
    op = list(map(int, input().split()))
    if op[0]==1:
        AddEdge(op[1], op[2],adjLst)
    else:
        Vertex(op[1],adjLst)