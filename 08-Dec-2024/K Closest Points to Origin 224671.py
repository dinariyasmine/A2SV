# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for (x,y) in points:
            distances.append((sqrt(x**2 + y**2), x, y))
        distances = sorted(distances, key=lambda x:x[0])
        
        ans = []
        for i in range(k):
            x1 = distances[i][1]
            y1 = distances[i][2]
            ans.append((x1, y1))
        
        return ans

        