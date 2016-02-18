# -*- coding: utf-8 -*-

'''
Number of Digit One
===================

Given an integer n, count the total number of digit 1 appearing in all
non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''


class Solution(object):
    '''算法思路：

    设我们要统计的的数字为 k，本题为 k=1

    根据观察，n 的每一位出现 k 的次数都有一下规律：

    当 该位 < k，那么出现 k 的次数为 (n / highBase) * base
    当 该位 == k，那么出现 k 的次数为 (n / highBase) * base + (n % base + 1)
    当 该位 > k，那么出现 k 的次数为 (n / highBase + 1) * base

    其中 base 为该位对应的 10 的 i 次方，highBase 为 10 的 i+1 次方
    当该位为个位时 i=1, 当该位为十位时 i=10，当该位为百位时 i=100......依次类推
    '''
    def countDigitOne(self, n):
        if n <= 0:
            return 0

        k, count, num, base, highBase = 1, 0, n, 1, 10
        while num:
            num, mod = divmod(num, 10)

            if mod < k:
                count += (n / highBase) * base
            elif mod == k:
                count += (n / highBase) * base + (n % base + 1)
            else:
                count += (n / highBase + 1) * base

            base *= 10
            highBase *= 10

        return count


s = Solution()
print s.countDigitOne(-1)



from operator import itemgetter

def count(num):
    '''计算一个数字中 1 的总个数，和各个位是否出现 1'''

    count, div, bits, i = 0, num, [0] * 10, 0
    while div:
        div, mod = divmod(div, 10)
        v = int(mod == 1)
        count += v
        bits[i] = v
        i += 1
    return count, bits


def total(num):
    counts = [count(i) for i in xrange(1, num + 1)]

    total = sum(map(itemgetter(0), counts))

    bits = map(itemgetter(1), counts)
    ge, shi, bai, qian = [sum(map(itemgetter(i), bits)) for i in xrange(4)]

    return total, qian, bai, shi, ge


for i in xrange(0, 1001):
    print total(i)[0], s.countDigitOne(i)

