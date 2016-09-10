# -*- coding: utf-8 -*-

'''
House Robber
============

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
'''


class Solution(object):
    '''算法思路：

    DP

    设 f(n) 为从 index=n 往后的最大和，则递推公式：

    f(n) = max(num[n] + f(n + 2), f(n + 1))

    不缓存结果，结果 TLE
    '''
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))


class Solution(object):
    '''算法思路：

    同上，只不过加上了缓存

    结果：AC
    '''
    def cache(f):
        def method(obj, cursor):
            record = getattr(obj, 'record', {})

            if not record:
                setattr(obj, 'record', record)

            if cursor not in record:
                record[cursor] = f(obj, cursor)

            return record[cursor]
        return method

    @cache
    def _rob(self, cursor):
        if cursor >= self.length:
            return 0

        if cursor == self.length - 1:
            return self.nums[cursor]

        if cursor == self.length - 2:
            return max(self.nums[cursor:])

        return max(
            self.nums[cursor] + self._rob(cursor + 2),
            self._rob(cursor + 1))

    def rob(self, nums):
        self.nums, self.length = nums, len(nums)
        return self._rob(0)


class Solution(object):
    '''算法思路：

    DP

    但是与上面相反，这里用数组保存已经遍历的结果

    设 f(n) 为从第 1 个数到第 n 个数的最大和，则递推公式为：

    f(n) = max(nums[n] + f(n - 2), f(n - 1))

    结果：AC
    '''
    def rob(self, nums):
        dp = [0] * (len(nums) + 2)
        for i in xrange(2, len(nums) + 2):
            dp[i] = max(nums[i - 2] + dp[i - 2], dp[i - 1])
        return dp[-1]


class Solution(object):
    '''算法思路：

    观察递推公式可得到，其实我们只需要两个变量 f(n-1)，f(n-2) 即可,
    可以不用数组来保存
    '''
    def rob(self, nums):
        fn_1 = fn_2 = 0
        for i in xrange(len(nums)):
            fn_1, fn_2 = max(fn_2 + nums[i], fn_1), fn_1
        return fn_1


s = Solution()
print s.rob([1, 7, 9, 2])
