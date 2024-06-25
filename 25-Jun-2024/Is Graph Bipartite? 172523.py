# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node,clr):
            # we color
            clrs[node] =clr
            #we check adj of the node
            for adj in graph[node]:
                #if not colored we color with opposite color 
                #node_color = 1 => adj_color = 0
                #node_color = 0 => adj_color = 1

                if clrs[adj] ==-1:  
                    #if it returns false it means that it's not bipatrite 
                    if not dfs(adj,1-clr):
                        return False
                #if we find node_color == adj_color it's not bipartie
                elif clrs[adj] == clr:
                    return False
            #no nodes adj colored with same color
            return True

        nbr_nodes=len(graph)
        # we init color of node with -1 => no node colored
        clrs = [-1]*nbr_nodes
        #we go throught the nodes
        for i in range(nbr_nodes):
            #if not colored
            if clrs[i] ==-1:
                #if it returns false it means that it's not bipatrite  
                if not dfs(i,0):  
                    return False
        return True
