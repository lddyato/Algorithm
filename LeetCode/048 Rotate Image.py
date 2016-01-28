# -*- coding: utf-8 -*-

'''
Rotate Image
============

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''


class Solution(object):
    '''算法思路：

    - o = (length - 1) / 2.0 旋转的中心为 (o, o)
    - 可以根据 当前点 (row, col) 算出 将要翻转的点为 (col, 2 * o - row)
    - 找出要翻转的圈的起点，然后进行一圈一圈的翻转
    '''
    def rotateCircle(self, matrix, o, start_row, start_col):
        row, col, cnt, pre = (
            start_row, start_col, 0, matrix[start_row][start_col])

        while 1:
            cnt += row == start_row and col == start_col

            if cnt > 1:
                return

            x, y = int(col), int(2 * o - row)

            matrix[x][y], pre = pre, matrix[x][y]
            row, col = x, y

    def rotate(self, matrix):
        length = len(matrix)

        if length <= 1:
            return

        o = (length - 1) / 2.0

        for start_row in xrange(int(o) + 1):
            for start_col in xrange(int(o) + (not length % 2)):
                self.rotateCircle(matrix, o, start_row, start_col)


s = Solution()
s.rotate([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

s.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
