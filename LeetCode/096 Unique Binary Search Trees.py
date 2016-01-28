# -*- coding: utf-8 -*-

'''
Given n, how many structurally unique BST's (binary search trees) that store
values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


class Solution(object):
    '''算法思路：

    1...n 中每个数字为 root，各个情况之和
    '''
    def cache(f):
        def method(obj, *args):
            record = getattr(obj, 'record', {})
            if not record:
                setattr(obj, 'record', record)

            key = '{}:{}'.format(*args)
            if key not in record:
                record[key] = f(obj, *args)
            return record[key]
        return method

    @cache
    def count(self, start, end):
        if start + 1 >= end:
            return max(end - start, 0) + 1

        return sum([
            self.count(start, i - 1) * self.count(i + 1, end)
            for i in xrange(start, end + 1)])

    def numTrees(self, n):
        return self.count(1, n)


s = Solution()
print s.numTrees(3)
