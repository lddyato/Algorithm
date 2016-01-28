# -*- coding: utf-8 -*-

'''
Sparse Matrix Multiplication
============================

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''


class Solution(object):
    '''算法思路：

    中规中矩的矩阵乘法

    结果：TLE
    '''
    def multiply(self, A, B):
        if not A or not B:
            return []

        return [[
            sum(map(lambda x: x[0] * x[1], zip(A[i], [row[j] for row in B])))
            for j in xrange(len(B[0]))]
            for i in xrange(len(A))]


class Solution(object):
    '''算法思路：

    先将稀疏矩阵压缩成三元二维数组，然后遍历三元二维数组，即可

    三元二维数组的结构为 [行，列，值]

    结果：AC
    '''
    def compress(self, matrix):
        return [
            [i, j, num]
            for i, row in enumerate(matrix)
            for j, num in enumerate(row) if num
        ]

    def multiply(self, A, B):
        (cpA, cpB), r = map(self.compress, (A, B)), [
            [0] * len(B[0]) for i in xrange(len(A))]

        [r[rowA].__setitem__(columnB, r[rowA][columnB] + numA * numB)
         for rowA, columnA, numA in cpA
         for rowB, columnB, numB in cpB if columnA == rowB]

        return r


A = [
    [1, 0, 0],
    [-1, 0, 3]
]

B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

s = Solution()
print s.multiply(A, B)
