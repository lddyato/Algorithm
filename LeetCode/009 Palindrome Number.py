# -*- coding: utf-8 -*-

'''
Palindrome Number
=================

Determine whether an integer is a palindrome. Do this without extra space.
'''


class Solution(object):
    '''算法思路：

    现将 integer 转换为 string，然后每次判断 string 的首尾，如果相等就将 x 去掉首尾
    否则不是回文

    注意：不要额外声明变量
    '''
    def isPalindrome(self, x):
        x = str(x)

        while x and x[0] == x[len(x) - 1]:
            x = x[1: len(x) - 1]

        return len(x) == 0


s = Solution()
print s.isPalindrome('')
