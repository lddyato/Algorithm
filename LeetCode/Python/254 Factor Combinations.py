# -*- coding: utf-8 -*-

'''
Factor Combinations
===================

Numbers can be regarded as product of its factors. For example,

    8 = 2 x 2 x 2;
      = 2 x 4.

Write a function that takes an integer n and return all possible combinations
of its factors.

Note:
- Each combination's factors must be sorted ascending, for example: The factors
  of 2 and 6 is [2, 6], not [6, 2].
- You may assume that n is always positive.
- Factors should be greater than 1 and less than n.

Examples:

input: 1
output:
[]

input: 37
output:
[]

input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
'''


class Solution(object):
    '''算法思路：

    递归
    '''
    def getFactors(self, n, start=2):
        r, sqrt = [], lambda x: int(pow(x, 0.5))
        for i in xrange(start, sqrt(n) + 1):
            div, mod = divmod(n, i)
            if not mod:
                r += [[i, div]]
                if sqrt(div) >= i:
                    r += [[i] + p for p in self.getFactors(div, i)]
        return r


class Solution(object):
    '''算法思路:

    同上，只不过 sqrt 用了 math
    '''
    def getFactors(self, n, start=2):
        import math

        r, sqrt = [], lambda x: int(math.sqrt(x))
        for i in xrange(start, sqrt(n) + 1):
            div, mod = divmod(n, i)
            if not mod:
                r += [[i, div]]
                if sqrt(div) >= i:
                    r += [[i] + p for p in self.getFactors(div, i)]
        return r


s = Solution()
print s.getFactors(12)
