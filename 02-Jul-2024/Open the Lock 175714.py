# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def concatene(nbrs):
            return ''.join(str(nbr) for nbr in nbrs)

        def strp(nbr):
            return [dgt for dgt in str(nbr)]

        if '0000' in deadends:
            return -1
        
        curr = '0000'
        visited = set([curr])
        dq = deque([(curr,0)])
        
        

        while dq:
            curr,cpt = dq.popleft()

            if  target == curr:
                return cpt 

            
            for i in range(4):
                for d in (-1,1):
                    dgt = (int(curr[i])+d) % 10
                    curr1 = curr[:i] + str(dgt) + curr[i+1:]
                    if curr1 not in visited and curr1 not in deadends:
                        dq.append((curr1,cpt+1))
                        visited.add(curr1)
            
        return -1
            

        



        

             

        
            
        