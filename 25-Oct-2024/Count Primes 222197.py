# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [1] * n
        for i in range(2, int(n**0.5) + 1):
            if prime[i] == 1:
                # if i is prime then all its multiples aren't
                for j in range(i*i, n, i):
                    prime[j] = 0
        
        cpt = 0
        for i in range(2, n):
            if prime[i] == 1:
                cpt += 1
        return cpt
        