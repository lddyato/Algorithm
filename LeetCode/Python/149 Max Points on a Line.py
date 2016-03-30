# -*- coding: utf-8 -*-

'''
Max Points on a Line
====================

Given n points on a 2D plane, find the maximum number of points that lie on the
same straight line.
'''


import collections


class Solution(object):
    '''算法思路：

    从集合中取出任意两点组成一条直线，然后将这两点加到该直线对应的集合中，最后找到每条
    直线对应的集合中点最多的那条直线，需要注意的有两点：

    - 原来的 points 中可能有重复的点
    - 生成的直线要用 a*y + b*x + c = 0 这种形式表示，因为如果用 y = k*x + b 这种形式
      表示，那么 k 和 b 有可能是小数，而小数之间的比较不能用 = 号比较，这就造成了 key
      的不稳定
    '''
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def genLine(self, p1, p2):
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = p2.x * p1.y - p1.x * p2.y

        if a < 0 or a == 0 and b < 0:
            a, b, c = -a, -b, -c

        _gcd = self.gcd(self.gcd(a, b), c)
        return a // _gcd, b // _gcd, c / _gcd

    def maxPoints(self, points):
        points = map(lambda p: (p.x, p.y), points)

        counter = collections.Counter(points)
        lines = collections.defaultdict(set)

        distinctPoints, n = counter.keys(), len(counter)
        if n < 3:
            return len(points)

        for i in range(n):
            for j in range(i + 1, n):
                pi, pj = distinctPoints[i], distinctPoints[j]
                lines[self.genLine(Point(*pi), Point(*pj))] |= {pi, pj}

        return max(
            sum([counter[p] for p in points]) for points in lines.values())


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


array = [[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]]
points = [Point(x, y) for x, y in array]


s = Solution()
print s.maxPoints(points)
