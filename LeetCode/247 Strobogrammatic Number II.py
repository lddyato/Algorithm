# -*- coding: utf-8 -*-

'''
Strobogrammatic Number II
=========================

A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
'''


class Solution(object):
    '''算法思路：

    递归生成，全排列

    需要注意的是：
    - 如果 n > 1，最外边不能是 0
    - 如果 n 是奇数，中间不能是 6, 9
    '''
    def getParts(self, step, max_step):
        original = ['1', '6', '8', '9']
        reverse = ['1', '9', '8', '6']

        if step != max_step:
            original.append('0')
            reverse.append('0')

        if step == 1:
            return original, reverse

        first, second = self.getParts(step - 1, max_step)
        first = [n + i for n in original for i in first]
        second = [i + n for n in reverse for i in second]

        return first, second

    def findStrobogrammatic(self, n):
        if n <= 0:
            return []

        if n == 1:
            return ['0', '1', '8']

        first, second = self.getParts(n/2, n/2)
        mids = ['0', '1', '8'] if n & 1 else ['']

        return [
            first[i] + mid + second[i]
            for mid in mids for i in xrange(len(first))
        ]


class Solution(object):
    '''算法思路：

    另外一种写法
    '''
    def search(self, n, low, high, path, r):
        if low > high:
            r.append(''.join(path))
            return

        maps = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        for k, v in maps:
            path[low], path[high] = k, v
            if not (low == 0 and path[low] == '0' and low != high) and (
                    low != high or low == high and k == v):
                self.search(n, low + 1, high - 1, path, r)


    def findStrobogrammatic(self, n):
        r = []
        self.search(n, 0, n - 1, [None] * n, r)
        return r


s = Solution()
print s.findStrobogrammatic(10)
