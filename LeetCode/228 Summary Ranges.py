# -*- coding: utf-8 -*-

'''
Summary Ranges
==============

Given a sorted integer array without duplicates, return the summary of its
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

class Solution(object):
    def add(self, r, start, i):
        r.append(start == i - 1 and str(self.nums[start]) or '{}->{}'.format(
                 self.nums[start], self.nums[i - 1]))

    def summaryRanges(self, nums):
        if not nums:
            return []

        self.nums = nums

        r, start = [], 0
        for i in xrange(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                continue

            self.add(r, start, i)
            start = i

        self.add(r, start, len(nums))
        return r


s = Solution()
print s.summaryRanges([1, 3])
