# -*- coding: utf-8 -*-

'''
Valid Palindrome
================

Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to
ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution(object):
    '''算法思路：

    两边加逼，找到首尾要比较的两个对象相比较
    '''
    def is_alphanumeric(self, c):
        return any(map(
            lambda i: i[0] <= c <= i[1], (('0', '9'), ('A', 'Z'), ('a', 'z'))))

    def isPalindrome(self, s):
        low, high = 0, len(s) - 1
        while low <= high:
            while low <= high and not self.is_alphanumeric(s[low]):
                low += 1

            while low <= high and not self.is_alphanumeric(s[high]):
                high -= 1

            if low > high:
                return True

            if s[low].lower() != s[high].lower():
                return False

            low += 1
            high -= 1

        return True


s = Solution()
print s.isPalindrome('')
