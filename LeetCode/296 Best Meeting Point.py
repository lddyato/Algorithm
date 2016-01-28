# -*- coding: utf-8 -*-

'''
Best Meeting Point
==================

A group of two or more people wants to meet and minimize the total travel
distance. You are given a 2D grid of values 0 or 1, where each 1 marks the
home of someone in the group. The distance is calculated using Manhattan
Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (0,2) is an ideal meeting point, as the total travel distance of
2+2+2=6 is minimal. So return 6.

Hint:

Try to solve it in one dimension first. How can this solution apply to the two
dimension case?
'''


import operator


class Solution(object):
    '''算法思路：

    分别解出一维空间上的点，然后合并成二维空间上的点，解一维空间可以用 O(n) 的算法，
    即 分别算出左右两侧距离和
    '''
    def minOneDimension(self, points):
        minimum, index, n, left, total = (
            float('inf'), None, len(points), 0, sum(points))

        for i, p in enumerate(points, 1):
            current = (p * (i - 1) - left) + (total - left - p * (n - i + 1))

            minimum, index = (
                current, p) if current < minimum else (minimum, index)
            left += p

        return index

    def minTotalDistance(self, grid):
        points = [
            (i, j) for i, row in enumerate(grid)
            for j, num in enumerate(row) if num]

        meetingPoint = map(
            self.minOneDimension,
            [sorted(map(operator.itemgetter(i), points)) for i in xrange(2)])

        return sum([
            abs(meetingPoint[0] - p[0]) + abs(meetingPoint[1] - p[1])
            for p in points])


s = Solution()
print s.minTotalDistance([
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,1,0],
    [1,1,0,0,0,0,1,0,0],
    [0,0,0,1,1,1,0,0,0]
])

# print s.minTotalDistance()
