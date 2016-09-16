# -*- coding: utf-8 -*-

'''
Set Matrix Zeroes
=================

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in place.

Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution(object):
    '''算法思路：

    把有 0 的行和列保存起来，然后遍历把相关的列和行设置为 0 即可

    Time: O(mn)
    Space: O(m + n)
    '''
    def setZeroes(self, matrix):
        if not matrix:
            return

        rows, cols = set(), set()

        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if v == 0:
                    rows.add(i)
                    cols.add(j)

        for r in rows:
            for j in xrange(len(matrix[0])):
                matrix[r][j] = 0

        for c in cols:
            for i in xrange(len(matrix)):
                matrix[i][c] = 0


class Solution(object):
    """算法思路：

    我们肯定要保存哪一行那一列要被置0, 但是其又要求constant space，因此我们
    可以考虑利用原matrix，用matrix的第0列和第0行保存信息

    Time: O(mn)
    Space: O(1)
    """
    def setZeroes(self, matrix):
        m, n = map(len, (matrix, matrix[0]))

        col0 = None
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] != 0:
                    continue

                matrix[i][0] = 0
                if j == 0:
                    col0 = 0
                else:
                    matrix[0][j] = 0

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in xrange(n):
                matrix[0][j] = 0

        if col0 == 0:
            for i in xrange(m):
                matrix[i][0] = 0
