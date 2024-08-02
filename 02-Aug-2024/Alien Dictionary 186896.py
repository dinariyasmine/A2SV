# Problem: Alien Dictionary - https://practice.geeksforgeeks.org/problems/alien-dictionary/1

#User function Template for python3
from collections import deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    
        def topological_sort(graph):
        
            in_deg = {node: 0 for node in graph}
            for node in graph:
                for vsn in graph[node]:
                    in_deg[vsn] += 1
            
           
            dq = deque([node for node in graph if in_deg[node] == 0])
            
            ordered = []
            
            while dq:
                node = dq.popleft()
                ordered.append(node)
                
                
                for vsn in graph[node]:
                    
                    in_deg[vsn] -= 1
                    
                    if in_deg[vsn] == 0:
                        dq.append(vsn)
            
            
            if len(ordered) == len(graph):
                return ordered
            else:
                return []
        graph = {
            chr(97 + i):[] for i in range(K)
        }
        
        
        
        
        for i in range(N - 1):
            for j in range(min(len(alien_dict[i]), len(alien_dict[i + 1]))):
                if alien_dict[i][j] != alien_dict[i + 1][j]:
                    graph[alien_dict[i][j]].append(alien_dict[i + 1][j])
                    break
        return topological_sort(graph)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends