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


class Solution(object):
    """算法思路：

    同上，不过是另外一种写法
    """
    def circle(self, matrix, x, y, w, h):
        r = []

        i, j = x, y
        for j in xrange(y, y + w):
            r.append(matrix[i][j])

        for i in xrange(x + 1, x + h):
            r.append(matrix[i][j])

        if h > 1 and w > 1:
            for j in xrange(y + w - 2, y - 1, -1):
                r.append(matrix[i][j])

        if w > 1 and h > 2:
            for i in xrange(x + h - 2, x, -1):
                r.append(matrix[i][j])

        return r

    def spiralOrder(self, matrix):
        if not matrix:
            return []

        r = []

        x, y, w, h = 0, 0, len(matrix[0]), len(matrix)
        while w > 0 and h > 0:
            r += self.circle(matrix, x, y, w, h)

            x += 1
            y += 1
            w -= 2
            h -= 2

        return r


s = Solution()
print s.spiralOrder([])
