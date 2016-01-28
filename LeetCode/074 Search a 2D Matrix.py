# -*- coding: utf-8 -*-

'''
Search a 2D Matrix
==================

Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous
row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true.
'''


class Solution(object):
    '''算法思路：

    依旧是二分查找
    '''
    def element(self, i, matrix, n):
        i, j = divmod(i, n)
        return matrix[i][j]

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])

        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) / 2
            midVal = self.element(mid, matrix, n)

            if midVal < target:
                low = mid + 1
            elif midVal > target:
                high = mid - 1
            else:
                return True

        return False
