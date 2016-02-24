# -*- coding: utf-8 -*-

'''
Search a 2D Matrix II
=====================

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''


class Solution(object):
    '''算法思路：

    将 matrix 划分为 4 个部分，分别为 左上、右上、左下、右下，左上一定比 mid 小，
    右下一定比 mid 大，左下 和 右上 不确定

    结果：TLE
    '''
    def search(self, matrix, leftTop, rightBottom, target, last):
        if leftTop == rightBottom:
            return matrix[leftTop[0]][leftTop[1]] == target

        m = rightBottom[0] - leftTop[0] + 1
        index = lambda x: (x[1] - leftTop[1]) * m + (x[0] - leftTop[0])

        i, j = map(
            sum, zip(divmod(
                index(leftTop) + index(rightBottom) >> 1, m)[::-1],leftTop))

        newLast = (leftTop, rightBottom, (i, j))
        if newLast == last:
            return False

        last = newLast

        leftBottom = (self.search(
            matrix, (i + 1, leftTop[1]), (rightBottom[0], j - 1), target, last)
            if i + 1 <= rightBottom[0] and j - 1 >= leftTop[1] else False)

        if leftBottom:
            return True

        rightTop = (self.search(
            matrix, (leftTop[0], j + 1), (i - 1, rightBottom[1]), target, last)
            if j + 1 <= rightBottom[1] and i - 1 >= leftTop[0] else False)

        if rightTop:
            return True

        if matrix[i][j] > target:
            return self.search(matrix, leftTop, (i, j), target, last)

        if matrix[i][j] < target:
            return self.search(matrix, (i, j), rightBottom, target, last)

        return True

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        return self.search(
            matrix, (0, 0), (len(matrix) -  1, len(matrix[0]) - 1),
            target, None)


class Solution(object):
    '''算法思路：

    从右上角搜索

    结果：AC
    '''
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False