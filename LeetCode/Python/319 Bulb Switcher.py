# -*- coding: utf-8 -*-

'''
Bulb Switcher
=============

There are n bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round, you toggle every
third bulb (turning on if it's off or turning off if it's on). For the nth
round, you only toggle the last bulb. Find how many bulbs are on after n
rounds.

Example:

    Given n = 3.

    At first, the three bulbs are [off, off, off].
    After first round, the three bulbs are [on, on, on].
    After second round, the three bulbs are [on, off, on].
    After third round, the three bulbs are [on, off, off].

    So you should return 1, because there is only one bulb is on.
'''


class Solution(object):
    '''算法思路：

    问题的本质在于对于第 i(1<=i<=n) 个灯泡，到最后其是否亮在于 i 的约数是否是奇数个，
    算出每个 i 的结果，返回亮的个数即可

    Time: O(n^2)

    结果：TLE
    '''
    def divisorCount(self, n):
        return sum([
            [1, 2][n / i != i]
            for i in xrange(1, int(pow(n, 0.5)) + 1) if not n % i])

    def bulbSwitch(self, n):
        return sum([self.divisorCount(i) & 1 for i in xrange(1, n + 1)])


class Solution(object):
    '''算法思路：

    观察法，从 1 到 100 打印出来本题的结果可以发现规律：

    1 3个
    2 5个
    3 7个
    4 9个
    5 11个
    .
    .
    .

    也就是说，最终结果 n 和 n连续出现的个数 c 的关系为 c = 2*n+1，根据等差和公式可以
    得到 c = sqrt(n+1) - 1，根据此公式得到的结果如果不是整数，那么取上限整数
    '''
    def bulbSwitch(self, n):
        import math
        return int(math.ceil(math.sqrt(n + 1) - 1))


class Solution(object):
    '''算法思路：

    换另外一种思考方式，灯泡 i 是否亮在于其约数的个数是否是奇数个。我们知道约数都是成对
    出现的，比如 8，1 x 8，2 x 4。只有 i 为平方数的时候约数个数才为奇数个，比如 9，
    1 x 9，3 x 3。因此我们只需要查一下在不大于 n 的数中有多少个平方数即可。
    '''
    def bulbSwitch(self, n):
        import math
        # return int(pow(n, 0.5))
        return int(math.sqrt(n))


s = Solution()
for i in xrange(1, 101):
    print s.bulbSwitch(i)
