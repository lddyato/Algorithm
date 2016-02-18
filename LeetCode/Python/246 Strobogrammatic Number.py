# -*- coding: utf-8 -*-

'''
Strobogrammatic Number
======================

A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is
represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''


class Solution(object):
    def isStrobogrammatic(self, num):
        maps = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        low, high = 0, len(num) - 1
        while low <= high:
            if num[low] not in maps or maps[num[low]] != num[high]:
                return False
            low += 1
            high -= 1
        return True


s = Solution()
print s.isStrobogrammatic('2')
