# -*- coding: utf-8 -*-

'''
Climbing Stairs
===============

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?
'''


class Solution(object):
    '''算法思路：

    假设 f(n) 为爬 n 阶楼梯不同的方法数，则 f(n) = f(n-1) + f(n - 2)，就是一个
    菲波那切数列

    递归

    结果：Time Limit Exceeded
    '''
    def climbStairs(self, n):
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution(object):
    '''算法思路：同上

    迭代

    结果：Accepted
    '''
    def climbStairs(self, n):
        pre, cur = 0, 1
        for i in xrange(n):
            cur, pre = cur + pre, cur
        return cur


class Solution(object):
    '''算法思路：

    利用排列组合，2 的次数最多出现 n / 2 次，于是 1、2 出现的次数为一个组合，总个数的
    全排列除以 1 和 2 的个数的全排列 之和，即为所求

    结果：Accepted
    '''
    def climbStairs(self, n):
        fab = (lambda n: reduce(
            lambda x, y: x * y, xrange(1, n + 1), 1) if n else 1)

        # leetcode 支持标准库，并且不用 import
        # fab = math.factorial

        return sum(
            fab(n - i) / fab(i) / fab(n - i * 2)
            for i in xrange(n / 2 + 1)
        ) if n else 0


s = Solution()
print s.climbStairs(1)
print [s.climbStairs(i) for i in xrange(10)]
