# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_n = bin(n)[2:]
        for i in range(1, len(binary_n)):
            if binary_n[i] == binary_n[i - 1]:
                return False
        return True
