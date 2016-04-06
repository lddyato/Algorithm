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


class Solution(object):
    '''算法思路：

    动态规划，dp[i][j] 表示从 i 到 j 的各种情况总个数，那么

    dp[i][j] = sum(dp[i][k - 1] * dp[k + 1][j] for k in i..j)

    Time: O(n^4)
    Space: O(n^2)

    结果：勉强AC
    '''
    def numTrees(self, n):
        dp = [[1] * (n + 1) for _ in range(n + 1)]

        for r in range(1, n + 1):
            for i in range(1, n + 1 - r):
                for j in range(i, n + 1):
                    dp[i][j] = sum([
                        (dp[i][k - 1] if k > i else 1) *
                        (dp[k + 1][j] if k < j else 1)
                        for k in range(i, j + 1)
                    ])

        return dp[1][n]


class Solution(object):
    '''算法思路：

    观察上面我们发现，长度相同，那么总个数相同，比如 1-5, 2-6, 3-7...根据这个规律，我们
    可以优化下。

    dp[i] 表示长度为 i 的总个数，那么

    dp[i] = sum(dp[k] * dp[i - k - 1] for k in 0..i-1)

    Time: O(n^2)
    Space: O(n)
    '''
    def numTrees(self, n):
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = sum(dp[k] * dp[i - 1 - k] for k in xrange(i))
        return dp[-1]


s = Solution()
print s.numTrees(3)
