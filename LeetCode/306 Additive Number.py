# -*- coding: utf-8 -*-

'''
Additive Number
===============

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the
first two numbers, each subsequent number in the sequence must be the sum of
the preceding two.

For example:

"112358" is an additive number because the digits can form an additive
sequence: 1, 1, 2, 3, 5, 8.

    1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

"199100199" is also an additive number, the additive sequence is:
1, 99, 100, 199.

    1 + 99 = 100, 99 + 100 = 199

Note: Numbers in the additive sequence cannot have leading zeros, so sequence
1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine
if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
'''

import collections


class Solution(object):
    '''算法思路：

    前两个数字固定，那么就可以判断整个序列，所以枚举前两个不同的数字即可
    '''
    def add(self, a, b):
        i, j, carry, r = len(a) - 1, len(b) - 1, 0, collections.deque()
        while i >= 0 or j >= 0:
            carry, mod = divmod(
                (int(a[i]) if i >= 0 else 0) +
                (int(b[j]) if j >= 0 else 0) + carry, 10)
            r.appendleft(mod)

            i -= 1
            j -= 1

        if carry:
            r.appendleft(carry)

        return ''.join(map(str, r))

    def check(self, a, b, num):
        if not num:
            return True

        sum = self.add(a, b)
        if num.startswith(sum):
            return self.check(b, sum, num[len(sum):])

        return False

    def isAdditiveNumber(self, num):
        return any(
            self.check(num[:i + 1], num[i + 1:j + 1], num[j + 1:])
            for i in xrange(len(num) - 2)
            for j in xrange(i + 1, len(num) - 1)
        )


s = Solution()
print s.isAdditiveNumber("11")
