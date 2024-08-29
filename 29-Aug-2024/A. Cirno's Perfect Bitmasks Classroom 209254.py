# Problem: A. Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
	num = int(input())
	ref = num & -num
	while (num == ref or (num & ref) == 0):
		ref += 1
	print(ref)