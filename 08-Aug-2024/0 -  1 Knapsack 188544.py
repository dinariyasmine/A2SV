# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        
        
        memo = [[None] * (W + 1) for _ in range(n)]
        def helper(idx, currW):
            if idx >= n or currW > W:
                return 0
            
            if memo[idx][currW] is None:
                not_pick = helper(idx + 1, currW)
                pick = 0
                if currW + wt[idx] <= W:
                    pick = val[idx] + helper(idx + 1, currW + wt[idx])
                memo[idx][currW] = max(not_pick, pick)
            return memo[idx][currW]
        
        return helper(0, 0)