# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

m = int(input())
array = list(map(int, input().split()))

pos = []
neg = []
for num in array:
    if num >= 0:
        pos.append(num)
    else:
        
        neg.append(num)


somme = sum(pos)

if somme % 2 == 1:
    print(somme)
    
    
    
    
else:
    
    minPos = float('inf')
    maxNeg = float('-inf')
    
    #we look for min odd pos or max odd neg and compare when adding/substracting to somme
    for p in pos:
        if p % 2 == 1:
            minPos = min(minPos,p)
    
    for n in neg:
        if n % 2 == 1:
            maxNeg = max(maxNeg,n)
    
    
    op = []
    
    if minPos :
        op.append(somme-minPos)
    if maxNeg :
        op.append(somme+maxNeg)
    
    print(max(op))
