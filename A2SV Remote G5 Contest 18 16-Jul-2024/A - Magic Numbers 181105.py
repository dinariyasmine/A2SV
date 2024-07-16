# Problem: A - Magic Numbers - https://codeforces.com/gym/528793/problem/A


def LI():return list(map(int, input()))
def LSI():return input().split(" ")
def LC():return input().split()
def I():return int(input())
def S(): return input()



t = S()

authorized = {'1','4'}
failed = False
coherent = False
for digit in t:
    if digit not in authorized:
        print('NO')
        failed = True
        break

if not failed:
    for i in range(len(t)):
        if (t[i]) == '4':
            if i == 0 :
                print('NO')
                coherent = True
                break
            if not coherent:
                if not((t[i-1])=='1' or (t[i-1])=='4' and (t[i-2]) == '1'):
                    coherent = True
                    print('NO')
                    break
            
            

    
if not failed and not coherent:
    print('YES')
    