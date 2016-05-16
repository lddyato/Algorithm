# -*-
coding: utf-8 -*-

'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
'''


class Solution(object):
    '''算法思路：

    普通的循环，一直除以 3
    '''
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        while n:
            n, mod = divmod(n, 3)
            if mod:
                return n == 0 and mod == 1
        return True


class Solution(object):
    '''算法思路：

    枚举 32 位数以内所有可能的值
    '''
    def isPowerOfThree(self, n):
        return n in {
            1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049,
            177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163,
            387420489, 1162261467
        }


class Solution(object):
    '''算法思路：

    看 log(n, 3) 是否是整数
    '''
    def isPowerOfThree(self, n):
        import math

        return n > 0 and abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10


class Solution(object):
    '''算法思路：

    对于 32 位以内的数，也可以用这种方法
    '''
    def isPowerOfThree(self, n):
        return n > 0 and not 3 ** 19 % n


s = Solution()
print s.isPowerOfThree(243)
