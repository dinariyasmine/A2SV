# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic = defaultdict(list)
            
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                dic[routes[i][j]].append(i)
            


        if source == target:
                return 0


        dq = deque([(source,0)])
        curr = source
        visited = set([source])
        vroutes = set()

        while dq and curr != target:
            curr, bus = dq.popleft()


            curri = dic[curr]

            if curr == target:
                return bus


            for idx in curri:
                if idx in vroutes:
                    continue
                vroutes.add(idx)
                for rt in routes[idx]:
                    if rt not in visited:
                        dq.append((rt,bus+1))
                        visited.add(rt)
        return -1
                    

            



        