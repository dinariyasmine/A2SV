# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def inter(n):
    primes = [i for i in range(2, n + 1) if prime(i)]    
    cpt2 = 0
    for i in range(2, n + 1):
        cpt = 0
        for p in primes:
            if p * p > i:  
                break
            if i % p == 0:  
                cpt += 1
                while i % p == 0:
                    i //= p
        if i > 1:  
            cpt += 1
        if cpt == 2:
            cpt2 += 1
            
    return cpt2

n = int(input())
result = inter(n)
print(result)
