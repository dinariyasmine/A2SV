# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = {}


        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}

            if b not in graph:
                graph[b] = {}

            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return float(-1)

            if src == dst:
                return float(1)

            visited.add(src)

            for neighbor, value in graph[src].items():
                if neighbor in visited:
                    continue

                result = dfs(neighbor, dst, visited)
                if result != float(-1):
                    return result * value
                    
            return float(-1)

        res = []
        for q in queries:
            res.append(dfs(q[0], q[1], set()))
        return res