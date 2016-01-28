# -*- coding: utf-8 -*-

'''
Range Sum Query 2D - Immutable
==============================

Given a 2D matrix matrix, find the sum of the elements inside the rectangle
defined by its upper left corner (row1, col1) and lower right corner
(row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
- You may assume that the matrix does not change.
- There are many calls to sumRegion function.
- You may assume that row1 ≤ row2 and col1 ≤ col2.
'''


class NumMatrix(object):
    '''算法思路：

    前缀和，保存每一行的前缀和

    build: O(m*n)
    query: O(m)

    space: O(n)

    结果：AC
    '''
    def __init__(self, matrix):
        self.sums = []

        for row in matrix:
            r = [0]
            [r.append(r[-1] + num) for num in row]
            self.sums.append(r)

    def sumRegion(self, row1, col1, row2, col2):
        return sum([
            self.sums[row][col2 + 1] - self.sums[row][col1]
            for row in xrange(row1, row2 + 1)])


'========================================================================'


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = end - start + 1
        self.mid = start + end >> 1

    def hasIntersection(self, i):
        return not (i.start > self.end or i.end < self.start)

    def contain(self, i):
        return self.start <= i.start and self.end >= i.end


class SegmentTreeNode(object):
    def __init__(self, val, rows, cols):
        self.val = val
        self.rows = rows
        self.cols = cols
        self.children = []


class SegmentTree(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.root = self.build(
            Interval(0, len(matrix) - 1),
            Interval(0, len(matrix[0]) - 1)) if matrix else None

    def build(self, rows, cols):
        if min(rows.length, cols.length) < 1:
            return

        if rows.length == 1 and cols.length == 1:
            return SegmentTreeNode(
                self.matrix[rows.start][cols.start], rows, cols)

        intervals = (
            (rows.start, rows.mid, cols.start, cols.mid),
            (rows.start, rows.mid, cols.mid + 1, cols.end),
            (rows.mid + 1, rows.end, cols.start, cols.mid),
            (rows.mid + 1, rows.end, cols.mid + 1, cols.end)
        )

        children = filter(None, [
            self.build(Interval(i, j), Interval(p, q))
            for i, j, p, q in intervals])

        root = SegmentTreeNode(sum([c.val for c in children]), rows, cols)
        root.children = children

        return root

    def query(self, rows, cols, root=None):
        root = root or self.root

        if not (rows.hasIntersection(root.rows) and
                cols.hasIntersection(root.cols)):
            return 0

        if rows.contain(root.rows) and cols.contain(root.cols):
            return root.val

        return sum([self.query(rows, cols, c) for c in root.children])


class NumMatrix(object):
    '''算法思路：

    用链表实现线段树

    build: O(m*n)
    query: O(log(m) * log(n))

    结果：TLE
    '''
    def __init__(self, matrix):
        self.tree = SegmentTree(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        return self.tree.query(Interval(row1, row2), Interval(col1, col2))


'========================================================================'


class NumMatrix(object):
    '''算法思路：

    预先计算出 (0, 0) 到 (i, j) 的和

    build: O(m*n)
    query: O(1)

    space: O(m*n)

    结果：AC
    '''
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        self.sums = [[0] * (n + 1) for _ in xrange(m + 1)]

        for i, row in enumerate(matrix):
            s = 0
            for j, num in enumerate(row):
                s += num
                self.sums[i + 1][j + 1] = self.sums[i][j + 1] + s

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.sums[row2 + 1][col2 + 1] +
            self.sums[row1][col1] -
            self.sums[row1][col2 + 1] -
            self.sums[row2 + 1][col1])


'========================================================================='


class BinaryIndexedTree(object):
    '''算法思路：

    树状数组
    '''
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        self.matrix = matrix
        self.sums = [[0] * (n + 1) for _ in xrange(m + 1)]

        self.build()

    def build(self):
        [operator.setitem(
            self.sums[row], col,
            self.sums[row][col] + self.matrix[i - 1][j - 1]
        )
        for row in xrange(1, len(self.sums))
        for col in xrange(1, len(self.sums[0]))
        for i in xrange(row + 1 - (row & -row), row + 1)
        for j in xrange(col + 1 - (col & -col), col + 1)]

    def sum(self, row, col):
        r, i = 0, row
        while i > 0:
            j = col
            while j > 0:
                r += self.sums[i][j]
                j -= j & -j
            i -= i & -i
        return r


class NumMatrix(object):
    def __init__(self, matrix):
        self.tree = BinaryIndexedTree(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.tree.sum(row2 + 1, col2 + 1) +
            self.tree.sum(row1, col1) -
            self.tree.sum(row1, col2 + 1) -
            self.tree.sum(row2 + 1, col1))


matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

numMatrix = NumMatrix(matrix)

print numMatrix.sumRegion(0, 1, 0, 3)
print numMatrix.sumRegion(1, 1, 2, 2)
print numMatrix.sumRegion(1, 2, 2, 4)
