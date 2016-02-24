# -*- coding: utf-8 -*-

'''
Meeting Rooms II
================

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
'''


import collections


class Solution(object):
    '''算法思路：

    抵消思想，求最大和

    参考了：https://leetcode.com/discuss/58720/c-solution-using-a-map-total-11-lines
    '''
    def minMeetingRooms(self, intervals):
        record = collections.defaultdict(int)
        for i in intervals:
            record[i.start] += 1
            record[i.end] -= 1

        rooms, maximus = 0, 0
        for k in sorted(record):
            rooms += record[k]
            maximus = max(maximus, rooms)

        return maximus


import heapq


class Solution(object):
    '''算法思路：

    最小堆，每次清理已经结束的可能，添加该可能否，再统计尚未结束的课程的个数
    '''
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda i: i.start)

        heap, r = [], 0
        for i in intervals:
            while heap and heap[0] <= i.start:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
            r = max(r, len(heap))
        return r


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '<Interval {} {}>'.format(self.start, self.end)

    def __repr__(self):
        return '<Interval {} {}>'.format(self.start, self.end)


s = Solution()
print s.minMeetingRooms([Interval(2, 11), Interval(6, 16), Interval(11, 16)])
