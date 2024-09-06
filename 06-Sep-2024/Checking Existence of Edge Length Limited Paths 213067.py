# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        queries = [(p, q, weight, idx) for idx, (p, q, weight) in enumerate(queries)]

        queries.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
        
        answer = [False] * len(queries)  
        parent = list(range(n))
        rank = [0] * n
        
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        
        edge_idx = 0  
        for p, q, weight, query_idx in queries:
            
            # we create the sets for each query that respect the limit
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < weight:
                u, v, dist = edgeList[edge_idx]
                union(u, v)
                edge_idx += 1
            
            
            if find(p) == find(q):
                answer[query_idx] = True

        return answer
