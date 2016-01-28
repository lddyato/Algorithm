# -*- coding: utf-8 -*-

'''
Missing Ranges
==============

Given a sorted integer array where the range of elements are [lower, upper]
inclusive, return its missing ranges.

For example,

given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
return ["2", "4->49", "51->74", "76->99"].
'''


class Solution(object):
    '''算法思路：

    遍历一遍即可

    Time: O(n)
    '''
    def findMissingRanges(self, nums, lower, upper):
        gen = lambda i, j: ['%s->%s' % (i + 1, j - 1), str(i + 1)][i == j - 2]

        nums = [lower - 1] + nums + [upper + 1]
        return [
            gen(nums[i - 1], nums[i])
            for i in xrange(1, len(nums)) if nums[i] - nums[i - 1] > 1
        ]


s = Solution()
print s.findMissingRanges([], 99, 99)
