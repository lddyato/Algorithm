# -*- coding: utf-8 -*-

'''
Container With Most Water
=========================

Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''


class Solution(object):
    '''算法思路：

    最朴素的思路，每两个之间相互比较，找出最大的

    Time: O(n^2)
    结果：TLE
    '''
    def maxArea(self, height):
        return max([
            (j - i) * min(height[i], height[j])
            for i in xrange(len(height) - 1)
            for j in xrange(i + 1, len(height))] or [0])


class Solution(object):
    '''算法思路：

    两者之间 water 的计算公式为，min(height[low], height[high]) * (high - low)，
    由于 high - low 是逐渐减小的，那么有可能取比目前更优解的关键在于 height[low] 和
    height[high] 两者之间的较小值，因此不断增大较小值，看有无更优解

    Time: O(n)
    结果: AC
    '''
    def maxArea(self, height):
        low, high, most = 0, len(height) - 1, 0
        while low < high:
            most = max(most, min(height[low], height[high]) * (high - low))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return most


s = Solution()
print s.maxArea([5,2,12,1,5,3,4,11,9,4])
