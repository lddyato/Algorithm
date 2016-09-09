# -*- coding: utf-8 -*-

"""
Guess Number Higher or Lower
============================

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results
(-1, 1, or 0):

    -1 : My number is lower
    1 : My number is higher
    0 : Congrats! You got it!

Example:

    n = 10, I pick 6.

    Return 6.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    """算法思路：

    典型的二分查找
    """
    def guessNumber(self, n):
        low, high, = 1, n
        while low <= high:
            mid = low + high >> 1
            judge = guess(mid)

            if judge == 0:
                return mid

            if judge < 0:
                high = mid - 1
            else:
                low = mid + 1
