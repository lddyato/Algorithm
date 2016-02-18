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
