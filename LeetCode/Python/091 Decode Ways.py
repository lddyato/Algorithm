# -*- coding: utf-8 -*-

'''
Decode Ways
===========

A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways
to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''


class Solution(object):
    '''算法思路：

    使用递归，把中间的结果都给缓存起来

    record: 从 key 到最后一位 decode ways 的个数

    结果：TLE
    '''
    def getRecord(self, key):
        self.record[key] = self.record.get(key, None) or self.count(key)
        return self.record[key]

    def count(self, pointer):
        if self.error:
            return 0

        if pointer > self.n - 1:
            return 1

        if pointer == self.n - 1:
            return 1 if '1' <= self.s[pointer] <= '9' else 0

        current, next = self.s[pointer], self.s[pointer + 1]
        if (current == '1' and '1' <= next <= '9' or
                current == '2' and '1' <= next <= '6'):
            return self.getRecord(pointer + 1) + self.getRecord(pointer + 2)

        if current in ['1', '2'] and next == '0':
            return self.getRecord(pointer + 2)

        if '1' <= current <= '9':
            return self.getRecord(pointer + 1)

        self.error = True
        return 0

    def numDecodings(self, s):
        n = len(s)
        if not n or n == 1 and s == '0':
            return 0

        if n == 1:
            return n

        self.s = s
        self.n = n
        self.error = False
        self.record = {}

        count = self.count(0)
        return 0 if self.error else count


class Solution(object):
    '''算法思路：

    利用 DP，dp[i] 表示从字符串开头到第 i 位(based 1) decode ways 个数，则从上往下
    需要过滤的条件是：

    - 最后两位位于 11~19 和 21~26 这两个区间时，dp[i] = dp[i-1] + dp[i-2]
    - 最后两位是 10 和 20 时，dp[i] = dp[i-2]
    - 最后一位位于 1~9 区间时，dp[i] = dp[i-1]
    - 最后一位是 0，dp[i] = 0
    '''
    def numDecodings(self, s):
        n = len(s)
        if not n:
            return 0

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = int(s[0] != '0')

        for i in xrange(2, n + 1):
            two, one = int(s[i-2 : i]), int(s[i-1])
            if 10 <= two <= 26:
                dp[i] = (dp[i-1] + dp[i-2]) if one else dp[i-2]
            elif 1 <= one <= 9:
                dp[i] = dp[i-1]

        return dp[-1]


s = Solution()
print s.numDecodings(
    '4673351343232714528787622144828949686814115978657763689251918941228645'
    '575658338815495647817194659971')
