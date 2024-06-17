# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int):
        def btrac(row):
            #when we reach the n row (that doesn't exist since we start from 0) we append a copy : mtx_
            if row==n:
                mtx_= ["".join(row) for row in mtx]
                res.append(mtx_)
                return
            
            for col in range(n):
                # we go through board col by col and check id the case is allowed
                if col in cols or (row - col) in d1 or (row + col) in d2:
                    continue
                #it is allowed ? => assign a queen and forbid cases
                mtx[row][col] = 'Q'
                cols.add(col)
                d1.add(row - col)
                d2.add(row + col)
                
                btrac(row + 1)

                #when we finish a path we pop the actual and put '.' to mean allowed

                mtx[row][col] = '.'
                cols.remove(col)
                d1.remove(row - col)
                d2.remove(row + col)
        


        res= []
        mtx=[['.']*n for _ in range(n)]
        cols= set()
        d1= set()
        d2= set()
        btrac(0)
        return res

