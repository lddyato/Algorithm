# -*- coding: utf-8 -*-

'''
N-Queens
========

The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''


class Solution(object):
    '''算法思路：

    DFS，这里用了位操作

    :Params:
      - x: 当前第几层，当前坐标为 (x, y)
      - maskCol: 当前列的状态, 第几位与当前坐标关系为 maskCol[y]
      - maskLDRU: 左下-右上这一条斜线的状态，与坐标关系: maskLDRU[x + y]
      - maskLURD: 左上-右下这一条斜线的状态，与坐标关系: maskLDRU[n - 1 + y - x]

    递归写法
    '''
    def search(self, x, maskCol, maskLDRU, maskLURD, n, r):
        for y in xrange(n):
            bitCol, bitLDRU, bitLURD = 1 << y, 1 << x + y, 1 << n - 1 + y - x

            if not (bitCol & maskCol or bitLDRU & maskLDRU or bitLURD & maskLURD):
                r[x][y] = 'Q'

                if x == n - 1:
                    self.r.append([''.join(row) for row in r])
                else:
                    self.search(
                        x + 1, maskCol | bitCol, maskLDRU | bitLDRU,
                        maskLURD | bitLURD, n, r)
                r[x][y] = '.'

    def solveNQueens(self, n):
        self.r = []
        self.search(0, 0, 0, 0, n, [['.'] * n for _ in xrange(n)])
        return self.r


class Solution(object):
    '''算法思路：

    同上，迭代写法
    '''
    def solveNQueens(self, n):
        r, stack, solution = [], [[0] * 5], [['.'] * n for _ in xrange(n)]

        while stack:
            x, y, maskCol, maskLDRU, maskLURD = stack.pop()
            solution[x][(n + y - 1) % n] = '.'

            bitCol, bitLDRU, bitLURD = 1 << y, 1 << x + y, 1 << n - 1 + y - x
            if not (bitCol & maskCol or bitLDRU & maskLDRU or bitLURD & maskLURD):
                solution[x][y] = 'Q'

                if x == n - 1:
                    r.append([''.join(row) for row in solution])
                else:
                    if y + 1 < n:
                        stack.append([x, y + 1, maskCol, maskLDRU, maskLURD])

                    stack.append([
                        x + 1, 0, maskCol | bitCol, maskLDRU | bitLDRU,
                        maskLURD | bitLURD])
                    continue

                solution[x][y] = '.'

            if y + 1 < n:
                stack.append([x, y + 1, maskCol, maskLDRU, maskLURD])

        return r


s = Solution()
print s.solveNQueens(4)
