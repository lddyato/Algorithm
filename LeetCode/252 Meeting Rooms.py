# -*- coding: utf-8 -*-

'''
Meeting Rooms
=============

Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
'''


class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i.start)

        return all(intervals[i].end <= intervals[i + 1].start
                   for i in xrange(len(intervals) - 1))
