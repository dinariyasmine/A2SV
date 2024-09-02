# Problem: E - Good Will Hunting - https://codeforces.com/gym/545837/problem/E

l, r = map(int, input().split())

a = l
b = r

for i in range((r - l).bit_length() - 1, -1, -1):
    
    if (a ^ b) & (1 << i) == 0:
        
        curr_a = a | (1 << i)  
        curr_b = b & ~(1 << i)  
        
        if curr_a <= b and curr_a <= r:  
            a = curr_a
        if curr_b >= a and curr_b >= l:  
            b = curr_b

print(a ^ b)
