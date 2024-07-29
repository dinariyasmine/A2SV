# Problem: C - Experiment - https://codeforces.com/gym/537575/problem/C

import heapq


t = int(input())
slots = []
rooms = 0
occup_rooms = []
av_rooms = []


for i in range(t):
    s, t, b = map(int, input().split())
    slots.append((s,t,b))

slots.sort(key=lambda x:x[0])

for slot in slots:
    s, t, b = slot
    
    for j in range(b):
        if len(av_rooms) > 0:
            heapq.heappush(occup_rooms, (t, av_rooms.pop()))
            
        elif len(av_rooms) == 0 and len(occup_rooms) > 0 and occup_rooms[0][0] < s :
            tp , rp = heapq.heappop(occup_rooms)
            heapq.heappush(occup_rooms, (t, rp))
        else:
            rooms += 1
            heapq.heappush(occup_rooms, (t, rooms))
print(rooms)
                
            
            
            
        
        
       
    

    
