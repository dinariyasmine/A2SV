# Problem: B - Network Topology - https://codeforces.com/gym/531416/problem/B

from collections import defaultdict
    
def tplg(n,m,edges):
    if m!=n-1 and m!=n:
        return "unknown topology"
    adjLst=defaultdict(list)
    #we create adjacency list
    for v, w in edges:
        adjLst[v].append(w)
        adjLst[w].append(v)
    #we calculate deg for each node
    dg=[0]*(n + 1)
    for node in adjLst:
        dg[node] = len(adjLst[node])
        
        
    if m==n:
        #ring
        #all nodes have two nodes adjencents ==> deg == 2
        if all(deg==2 for deg in dg if deg>0):
            return "ring topology"
        
    elif m ==n-1:
        #bus
        #dg.count(1)==2 ==> means two nodes have a deg =1 (endpoints)
        #dg.count(2)==n-2==> means all other nodes (intermidiate) have a deg =2 
        if dg.count(1)==2 and dg.count(2)==n-2:
            return "bus topology"
        #star
        #dg.count(n-1)==1 for the head 
        #dg.count(1)==n-1 for all the others
        if dg.count(1)==n-1 and dg.count(n-1)== 1:
            return "star topology"
    #unkown 
    return "unknown topology"

n,m=map(int, input().split())
edges=[]
for _ in range(m):
    v,w=map(int, input().split())
    edges.append((v,w))
i=tplg(n,m,edges)
print(i)
