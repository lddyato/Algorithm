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

    二分

    Time: O(log(m*n))
    '''
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        low, high = 0, m * n - 1
        while low <= high:
            mid = low + high >> 1
            i, j = divmod(mid, n)

            if matrix[i][j] < target:
                low = mid + 1
            elif matrix[i][j] > target:
                high = mid - 1
            else:
                return True
        return False


class Solution(object):
    '''算法思路：

    二分

    Time: O(log(m) + log(n))
    '''
    def search(self, nums, target):
        low, high, n = 0, len(nums) - 1, len(nums)
        while low <= high:
            mid = low + high >> 1
            if nums[mid] > target:
                high = mid - 1
            else:
                if mid == n - 1 or nums[mid + 1] > target:
                    return mid
                low = mid + 1
        return -1

    def searchMatrix(self, matrix, target):
        row = self.search([row[0] for row in matrix], target)
        row = matrix[i] if row != -1 else []

        i = bisect.bisect_left(row, target)
        return i < len(row) and row[i] == target


class Solution(object):
    '''算法思路：

    Time: O(m + n)
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
