# -*- coding: utf-8 -*-

'''
Spiral Matrix
=============

Given a matrix of m x n elements (m rows, n columns), return all elements of
the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
'''


class Solution(object):
    '''算法思路：

    一圈一圈的遍历，需要注意的是 width != height 时的情况
    '''
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        row, col, width, height, r = 0, 0, len(matrix[0]), len(matrix), []
        while width > 0 and height > 0:
            i = j = 0
            for index, iterator in enumerate([
                    xrange(width),
                    xrange(1, height),
                    [[], xrange(width - 2, -1, -1)][height != 1],
                    [[], xrange(height - 2, 0, -1)][width != 1]]):
                for x in iterator:
                    if index & 1:
                        i = x
                    else:
                        j = x
                    r.append(matrix[row + i][col + j])
            row += 1
            col += 1
            width -= 2
            height -= 2
        return r


s = Solution()
print s.spiralOrder([])
