# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
  def maxProduct(self, words: List[str]) -> int:
    ans = 0

    def Mask(word):
      mask = 0
      for ch in word:
        mask |= 1 << ord(ch) - ord('a')
      return mask

    masks = [Mask(word) for word in words]

    for i in range(len(words)):
      for j in range(i, len(words)):
        # all positions end up = 0 when we do the "&" 101 & 010 = 000
        if not (masks[i] & masks[j]):
          ans = max(ans, len(words[i]) * len(words[j]))

    return ans