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


class Solution(object):
    '''算法思路：

    抵消思想，求最大和

    参考了：https://leetcode.com/discuss/58720/c-solution-using-a-map-total-11-lines
    '''
    def minMeetingRooms(self, intervals):
        import collections

        record = collections.defaultdict(int)
        for i in intervals:
            record[i.start] += 1
            record[i.end] -= 1

        rooms, maximus = 0, 0
        for k in sorted(record):
            rooms += record[k]
            maximus = max(maximus, rooms)

        return maximus


class Solution(object):
    '''算法思路：

    最小堆，贪心思想，开始最早的先使用教室，结束最早的最先被占用，如果冲突那就另外开一
    个教室

    参考了：https://leetcode.com/discuss/58926/python-heapq-solutions-with-explanation
    '''
    def minMeetingRooms(self, intervals):
        import heapq

        heap = []
        intervals.sort(key=lambda i: i.start)
        for i in intervals:
            (heapq.heappush if not heap or i.start < heap[0] else
                heapq.heapreplace)(heap, i.end)
        return len(heap)



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
