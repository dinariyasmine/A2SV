# Problem: A - Divide Array - https://codeforces.com/gym/505936/problem/A


n = int(input())

arr = sorted(list(map(int, input().split())))

#print negative
print(1,arr[0])
arr.pop(0)

#print(positive)
if arr[-1] > 0:
    print(1, arr[-1] )
    arr.pop( -1 )
else:
    print(2,arr[0],arr[1])
    arr.pop(0)
    arr.pop(0)

#print rest
print(len(arr),*arr)