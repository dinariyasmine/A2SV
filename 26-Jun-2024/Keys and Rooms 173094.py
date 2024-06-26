# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(idx):
            if idx in visited :
                return 
            visited.add(idx)
            for key in rooms[idx]:
                dfs(key)
            


        dfs(0)
        return  len(visited)==len(rooms)
            

        