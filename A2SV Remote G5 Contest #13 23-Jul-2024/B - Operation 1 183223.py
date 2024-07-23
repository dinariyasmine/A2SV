# Problem: B - Operation 1 - https://codeforces.com/gym/521860/problem/B

a, m = map(int, input().split())

op2 = a //2
op1 = a %2
ans = -1

while op2 >= 0:
    
    if (op2 + op1) % m == 0:
        ans = op2 + op1
        break
    
    op2 -=1
    op1 +=2

print(ans)
