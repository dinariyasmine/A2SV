# Problem: B - Catch Overflow! - https://codeforces.com/gym/520112/problem/B

t = int(input())
maxi = 2**32 - 1
x = 0
loops = [1]  

for _ in range(t):
    op = input().strip()

    if op == 'add':
        x += loops[-1]
        if x > maxi:
            print('OVERFLOW!!!')
            exit()

    elif op.startswith('for'):
        v = int(op.split()[1])
        
        curr = loops[-1] * v
        
        if curr > maxi:
            curr = maxi + 1  
        loops.append(curr)
        
    elif op == 'end':
        loops.pop()

print(x)
