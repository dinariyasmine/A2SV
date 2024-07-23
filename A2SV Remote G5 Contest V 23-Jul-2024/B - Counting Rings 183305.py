# Problem: B - Counting Rings - https://codeforces.com/gym/508510/problem/B

gandalf = input()
curr = 0
rings = 0
for i in range(len(gandalf)):
    if gandalf[i] == 'O':
        
        curr += 1
        
        rings = max (rings,curr)
        
    else:
        curr = 0
print(rings)