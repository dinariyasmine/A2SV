# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        size = [1 for i in range(26)]

        def union(node1, node2):
            node1 = ord(node1) - 97 
            node2 = ord(node2) - 97
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return
            if size[par1] > size[par2]:
                parent[par2] = par1
                size[par1] += size[par2]
            else:
                parent[par1] = par2
                size[par2] += size[par1]

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])  
            return parent[node]

        for query in equations:
            node1, node2 = query[0], query[-1]
            condition = query[1]

            if condition == '=':
                union(node1, node2)

        for query in equations:
            node1, node2 = query[0], query[-1]
            condition = query[1]

            if condition == '!':
                if find(ord(node1) - 97) == find(ord(node2) - 97):  
                    return False

        return True
