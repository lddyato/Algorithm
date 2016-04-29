# -*- coding: utf-8 -*-

'''
You are given an array x of n positive numbers. You start at point (0,0) and
moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to
the south, x[3] metres to the east and so on. In other words, after each move
your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path
crosses itself, or not.

Example 1:
Given x = [2, 1, 1, 2],
┌───┐
│   │
└───┼──>
    │

Return true (self crossing)
Example 2:
Given x = [1, 2, 3, 4],
┌──────┐
│      │
│
│
└────────────>

Return false (not self crossing)
Example 3:
Given x = [1, 1, 1, 1],
┌───┐
│   │
└───┼>

Return true (self crossing)
'''


class Solution(object):
    '''算法思路：

    不相交的的充分必要条件是: 形成的形状是螺旋形，分为外旋和内旋，分为两种情况：
      - 先外旋，后内旋
      - 只有内旋
    根据这两种情况进行分析即可，需要注意的是第一种情况交接的时候的处理
    '''
    def isSelfCrossing(self, x):
        n = len(x)
        if n < 4:
            return False

        if x[0] - x[2] >= 0 and x[3] - x[1] >= 0:
            return True

        i = 4
        if x[3] == x[1]:
            x[2] -= x[0]

        elif x[3] > x[1]:
            while i < n and x[i] > x[i - 2]:
                i += 1

            if i == n:
                return False

            if x[i] >= x[i - 2] - x[i - 4]:
                x[i - 1] -= x[i - 3]
                i += 1

        while i < n and x[i] < x[i - 2]:
            i += 1

        return i != n


s = Solution()
print s.isSelfCrossing([1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1])
