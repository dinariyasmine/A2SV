# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        #contruct graph adjacency list 
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)

        def dfs(node, target, visited):
            if node == target:
                return True
            visited.add(node)

            for nodei in graph[node]:
                #if we didn't visit the node 
                if nodei not in visited:
                    if dfs(nodei, target, visited):
                        return True
            return False

        return dfs(source, destination, set())






        