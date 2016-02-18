# -*- coding: utf-8 -*-

'''
Ugly Number
===========

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime
factor 7.

Note that 1 is typically treated as an ugly number.
'''


class Solution(object):
    def isPrime(self, num):
        for i in xrange(2, int(pow(num, 0.5)) + 1):
            if not num % i:
                return False
        return True

    def isUgly(self, num):
        if num <= 0:
            return False

        if num == 1:
            return True

        if self.isPrime(num) and num not in [2, 3, 5]:
            return False

        for i in xrange(2, int(pow(num, 0.5)) + 1):
            div, mod = divmod(num, i)
            if not mod and ((
                    self.isPrime(div) and div not in [2, 3, 5]) or (
                    self.isPrime(i) and i not in [2, 3, 5])):
                return False

        return True


s = Solution()
print s.isUgly(50)
