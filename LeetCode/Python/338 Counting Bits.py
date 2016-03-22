# -*- coding: utf-8 -*-

"""
Given a non negative integer number num. For every numbers i in the range
0 ≤ i ≤ num calculate the number of 1's in their binary representation and
return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

- It is very easy to come up with a solution with run time O(n*sizeof(integer)).
  But can you do it in linear time O(n) /possibly in a single pass?
- Space complexity should be O(n).
- Can you do it like a boss? Do it without using any builtin function like
   __builtin_popcount in c++ or in any other language.
"""

class Solution(object):
    '''算法思路：

    分别算出每一个数的 1 的个数

    Time: O(n*sizeof(integer))
    Space: O(1)
    '''
    def count(self, num):
        cnt = 0
        while num:
            cnt += num & 1
            num >>= 1
        return cnt

    def countBits(self, num):
        return [self.count(i) for i in range(num + 1)]


class Solution(object):
    '''算法思路：

    发现规律，每个数字的 1 的个数为除去最高位 1 后对应的数字的 1 的个数 + 1

    比如 13 = 0b1101，除去最高位为 0b101 = 5，然后 5 中 1 的个数 + 1，依次类推

    Time: O(n)
    Space: O(n)
    '''
    def countBits(self, num):
        r, base = [0, 1] + [0] * (num - 1), 1
        for i in range(2, num + 1):
            r[i] = r[i % base] + 1
            if base << 1 == i:
                base <<= 1
        return r[:num + 1]
