# -*- coding: utf-8 -*-

'''
Maximal Rectangle
=================

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing all ones and return its area.
'''


class Solution(object):
    '''算法思路：

    在 Largest Rectangle in Histogram 的基础之上，每向下移动一行，同时更新 height
    '''
    def rectangle(self, height):
        stack, r = [-1], 0
        for i, h in enumerate(height):
            while h < height[stack[-1]]:
                r = max(height[stack.pop()] * (i - stack[-1] - 1), r)
            stack.append(i)
        return r

    def maximalRectangle(self, matrix):
        height, r = [0] * ((matrix and len(matrix[0]) or 0) + 1), 0
        for row in matrix:
            for j, v in enumerate(row):
                height[j] = height[j] + 1 if v == '1' else 0
            r = max(self.rectangle(height), r)
        return r


s = Solution()
print s.maximalRectangle([])
