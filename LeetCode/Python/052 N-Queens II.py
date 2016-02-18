# -*- coding: utf-8 -*-

'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of
distinct solutions.
'''


class Solution(object):
    '''算法思路:

    同 I, 不过只计数，递归写法
    '''
    def search(self, x, maskCol, maskLDRU, maskLURD, n, r):
        for y in xrange(n):
            bitCol, bitLDRU, bitLURD = 1 << y, 1 << x + y, 1 << n - 1 + y - x

            if not (bitCol & maskCol or bitLDRU & maskLDRU or bitLURD & maskLURD):
                r[x][y] = 'Q'

                if x == n - 1:
                    self.r += 1
                else:
                    self.search(
                        x + 1, maskCol | bitCol, maskLDRU | bitLDRU,
                        maskLURD | bitLURD, n, r)
                r[x][y] = '.'

    def totalNQueens(self, n):
        self.r = 0
        self.search(0, 0, 0, 0, n, [['.'] * n for _ in xrange(n)])
        return self.r


class Solution(object):
    '''算法思路：

    同 I, 不过只计数，迭代写法
    '''
    def totalNQueens(self, n):
        r, stack, solution = 0, [[0] * 5], [['.'] * n for _ in xrange(n)]

        while stack:
            x, y, maskCol, maskLDRU, maskLURD = stack.pop()
            solution[x][(n + y - 1) % n] = '.'

            bitCol, bitLDRU, bitLURD = 1 << y, 1 << x + y, 1 << n - 1 + y - x
            if not (bitCol & maskCol or bitLDRU & maskLDRU or bitLURD & maskLURD):
                solution[x][y] = 'Q'

                if x == n - 1:
                    r += 1
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
