# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        knightMoves =[(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2),(-1, 2),(1, -2),(-1, -2)]
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j] = 1



        for m in range(1, k + 1):
            new_dp = [[0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    proba = 0


                    for move in knightMoves:
                        curr_i = i + move[0]
                        curr_j = j + move[1]
                        if 0 <= curr_i < n and 0 <= curr_j < n:
                            proba += dp[curr_i][curr_j]
                    new_dp[i][j] = proba / 8
                    
            dp = new_dp
        return dp[row][column]
