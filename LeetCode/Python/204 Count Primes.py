# -*- coding: utf-8 -*-

'''
Count Primes
============

Description:

Count the number of prime numbers less than a non-negative number, n.
'''


class Solution(object):
    '''算法思路：

    依次计算是否是素数

    Time: O(n^2)

    结果：TLE
    '''
    def isPrime(self, num):  # 费马小定理
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        for p in primes:
            if p != num and not pow(num, p - 1) % p == 1:
                return False
        return True

    def isPrime(self, num):  # common way
        for i in range(2, int(pow(num, 0.5)) + 1):
            if not num % i:
                return False
        return True

    def countPrimes(self, n):
        return sum([self.isPrime(num) for num in range(n)])


class Solution(object):
    '''算法思路：

    Sieve Of Eratosthenes，埃拉托斯特尼筛法，简称埃氏筛aishisaixuan
    '''
    def countPrimes(self, n):
        nums = range(n)
        for i in xrange(2, int(pow(n, 0.5)) + 1):
            if nums[i] is None:
                continue

            times = i
            while times * i < n:
                nums[times * i] = None
                times += 1

        return max(len(nums) - 2 - nums.count(None), 0)


s = Solution()
print s.countPrimes(50)
