# Problem: A - Flag - https://codeforces.com/gym/531416/problem/A

def row_vrf(row):
    ref = row[0]
    for j in range(len(row)):
        if row[j]!= ref:
            return False      
    return True
n, m=map(int,input().split())
mtx =[]
x = True
used= set()

for i in range(n):
    row= list(input().strip())
    if not row_vrf(row):
        print('NO')
        x = False
        break
    mtx.append(row)
if x:
    w =True
    for k in range(1, n):
        if mtx[k][0]== mtx[k-1][0]:
            print('NO')
            w= False
            break
    if w:
        print('YES')
