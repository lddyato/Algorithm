# -*- coding: utf-8 -*-

'''
Strobogrammatic Number III
==========================

A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the
range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three
strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are
represented as string.
'''


class Solution(object):
    '''算法思路：

    DFS 遍历，并对结果进行筛选，看是否符合要求
    '''
    def search(self, n, start, end, low, high, path):
        if low > high:
            number = ''.join(path)
            self.count += not (
                len(start) == n and number < start or
                len(end) == n and number > end)
            return

        maps = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        for k, v in maps:
            path[low], path[high] = k, v

            part = ''.join(path[:low + 1])
            if (low == 0 and path[low] == '0' and low != high or
                    n == len(start) and part < start[:low + 1] or
                    n == len(end) and part > end[:low + 1]):
                continue

            if low != high or low == high and k == v:
                self.search(n, start, end, low + 1, high - 1, path)

    def strobogrammaticInRange(self, low, high):
        self.count = 0
        for n in xrange(len(low), len(high) + 1):
            self.search(n, low, high, 0, n - 1, [None] * n)
        return self.count


s = Solution()
print s.strobogrammaticInRange('1001', '11111')
