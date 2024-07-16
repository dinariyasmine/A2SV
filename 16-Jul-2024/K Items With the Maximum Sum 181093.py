# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        somme = 0
        for i in range(k):
            if numOnes>0:
                numOnes -= 1
                somme += 1
            elif numZeros>0:
                numZeros-= 1
                somme += 0
            elif numNegOnes>0:
                numNegOnes-= 1
                somme -= 1
            
        return somme


        
        