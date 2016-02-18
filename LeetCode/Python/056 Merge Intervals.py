# -*- coding: utf-8 -*-

'''
Merge Intervals
===============

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''


class Solution(object):
    '''算法思路：

    排序，遇到区间问题大多需要排序
    '''
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)
        r = []

        for i in intervals:
            if not r or i.start > r[-1].end:
                r.append(i)
            elif i.end > r[-1].end:
                r[-1].end = i.end

        return r


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '<Interval start={} end={}>'.format(self.start, self.end)


s = Solution()
intervals = [Interval(1, 4), Interval(2, 3)]

print s.merge(intervals)
