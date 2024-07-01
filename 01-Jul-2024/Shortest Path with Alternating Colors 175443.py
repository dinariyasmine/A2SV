# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:


        red = defaultdict(list)
        
        for u, v in redEdges:
            red[u].append(v)

        blue = defaultdict(list)

        for u, v in blueEdges:
            blue[u].append(v)
        
        distR =[-1]* n
        distB =[-1] * n
        
        # 0 => red 
        # 1 => blue
        dq = deque([(0,0),(0,1)]) #starting from the node with blue and red 

        distR[0] = 0

        distB[0] = 0
        
        
        while dq:
            node,clr=dq.popleft()
            
            if clr==0:  
                for ngh in red[node]:
                    if distB[ngh] ==-1:  
                        distB[ngh] =distR[node]+1
                        dq.append((ngh,1))  
            else:  
                for ngh in blue[node]:
                    if distR[ngh] ==-1:  
                        distR[ngh] =distB[node] + 1
                        dq.append((ngh,0))  
        
        
        res = [-1]*n


        for i in range(n):

            if distR[i] !=-1 and distB[i] !=-1:
                #we take the shortest choice
                res[i] = min(distR[i], distB[i])

            elif distR[i]!= -1:
                res[i] = distR[i]

            elif distB[i] != -1:
                res[i] = distB[i]
        
        return res