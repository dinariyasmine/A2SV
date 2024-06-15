# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

n = int(input())
idx = set()
mtx=[]
edges = []
for _ in range(n):
    row= list(map( int, input().split()) )
    mtx.append(row)
for i in range(len(mtx)):
    row = mtx[i]
    for j in range(len(row)):
        if row[j]==1 and (i,j) not in idx and (j,i) not in idx :
            edge = (i,j)
            idx.add(edge)
        
print(len(idx))



