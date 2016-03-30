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

    Time: O(m*n)
    '''
    def maxLineRectangle(self, heights):
        stack, r = [-1], 0
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                r = max(r, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        return r

    def maximalRectangle(self, matrix):
        heights, r = [0] * ((len(matrix[0]) if matrix else 0) + 1), 0
        for row in matrix:
            for j, val in enumerate(row):
                heights[j] = 0 if val == '0' else (heights[j] + 1)
            r = max(r, self.maxLineRectangle(heights))
        return r


s = Solution()
print s.maximalRectangle([])
