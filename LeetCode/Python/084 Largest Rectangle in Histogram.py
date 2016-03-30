# -*- coding: utf-8 -*-

'''
Largest Rectangle in Histogram
==============================

Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''


class Solution(object):
    '''算法思路：

    分治法，找到最小的 index，分别算出左右两边的最大 Rectangle，最终得出结果

    结果：TLE
    '''
    def findMin(self, height):
        r, index = float('inf'), None
        for i, h in enumerate(height):
            if h < r:
                r, index = h, i
        return r, index

    def largestRectangleArea(self, height):
        if not height:
            return 0

        if len(height) == 1:
            return height[0]

        h, index = self.findMin(height)
        return max(
            h * len(height), self.largestRectangleArea(height[:index]),
            self.largestRectangleArea(height[index + 1:]))


class Solution(object):
    '''算法思路：

    上述解法当查找左右边界的是否会出现重复比较的情况，可以考虑去掉重复比较

    以每个元素为高度，左右扩展，一直到两边都遇到比该元素小的元素为止，得到宽度，高宽
    相乘，如此这样，对每一个元素施以此措施。平均复杂度为 O(n^2)

    这里辅以栈，栈里边自底向上是递增数列，这样栈里边每一个元素的紧挨着的下边都是其
    左边界，遍历 height 的每一个元素，若当前元素小于栈顶元素，则说明当前元素是其右边界，
    一直弹栈，直到当前元素不小于栈顶元素。中间比较 Rectangle 面积大小。

    此算法来源于上面，但是把比较的结果以某种巧妙的方式保存到了栈中，栈顶是高，当前位置是右边
    界，栈顶的下面是左边界

    复杂度分析：每个元素最多 append，pop 一次，因此是 O(n)

    Time: O(n)
    结果：AC
    '''
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, r = [-1], 0

        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                r = max(r, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        return r


s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])
