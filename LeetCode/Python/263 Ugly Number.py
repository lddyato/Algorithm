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
    '''算法思路：

    每个数都可以表示为 1个或多个素数的积，因此除掉所有的 2，3，5 看剩下的是否是1即可
    '''
    def isUgly(self, num):
        if num <= 0:
            return False

        for p in [2, 3, 5]:
            while num % p == 0:
                num //= p
        return num == 1


class Solution(object):
    '''算法思路：

    对每一个因数判断其是否是不为 [2, 3, 5] 的素数
    '''
    condidates = {1, 2, 3, 5}

    def isPrime(self, num):
        for i in range(2, int(pow(num, 0.5)) + 1):
            if num % i == 0:
                return False
        return True

    def isUgly(self, num):
        if num <= 0:
            return False

        for i in range(1, int(pow(num, 0.5)) + 1):
            div, mod = divmod(num, i)
            if mod == 0 and (
                    self.isPrime(i) and i not in self.condidates or
                    self.isPrime(div) and div not in self.condidates):
                return False
        return True


class Solution(object):
    '''算法思路：

    同上，不过运用了费马小定理

    N^(P - 1) % P = 1
    (X * Y) % Z = ((X % Z) * (Y % Z)) % Z
    '''
    condidates = {1, 2, 3, 5}
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    def isPrime(self, num):
        for p in self.primes:
            if p >= num:
                break

            if pow(num, p - 1) % p != 1:
                return False
        return True

    def isUgly(self, num):
        if num <= 0:
            return False

        for i in range(1, int(pow(num, 0.5)) + 1):
            div, mod = divmod(num, i)
            if mod == 0 and (
                    self.isPrime(i) and i not in self.condidates or
                    self.isPrime(div) and div not in self.condidates):
                return False
        return True


s = Solution()
print s.isUgly(50)
