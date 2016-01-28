# -*- coding: utf-8 -*-

'''
Trapping Rain Water
===================

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''


class Solution(object):
    '''算法思路：

    从左向右，分别以每个高度 h1 为参考，找到第一个不比该高度低的另外一个高度 h2，然后
    算出 h1 和 h2 之间能够 trap 的和，如果找不到 h2，说明此时 h1 是整个序列里边高度
    最高的，这时反过来查找另一个半，最后把所有 trap 的和相加起来即为所求
    '''
    def trap(self, height):
        i, result, length = 0, 0, len(height)
        while i < length - 2:
            j, s = i + 1, 0
            while j < length and height[j] < height[i]:
                s += height[j]
                j += 1

            if j == length:
                return result + self.trap(height[i:][::-1])

            result += (j - i - 1) * height[i] - s
            i = j

        return result


s = Solution()
s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
s.trap([4, 2, 3])
