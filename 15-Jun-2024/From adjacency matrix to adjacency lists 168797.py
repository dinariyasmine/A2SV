# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

def f(n, mtx):
    adjLst=[]
    for i in range(n):
        
        edges=[]
        for j in range(n):
            if mtx[i][j]==1:
                edges.append(j+1)  
        edges.sort() 
        adjLst.append( edges)
    return adjLst

n =int(input() )
mtx =[]
for _ in range(n):
    row= list(map( int, input().split()) )
    mtx.append(row)
adjLst = f(n, mtx)
for edges in adjLst:
    print(len(edges),' '.join( map(str, edges)))
