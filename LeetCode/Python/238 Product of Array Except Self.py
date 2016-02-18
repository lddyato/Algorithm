# -*- coding: utf-8 -*-

'''
Product of Array Except Self
============================

Given an array of n integers where n > 1, nums, return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:

Could you solve it with constant space complexity? (Note: The output array does
not count as extra space for the purpose of space complexity analysis.)
'''


class Solution(object):
    '''算法思路：

    预先计算出 从前往后 和 从后往前 的积，然后 i 的两边相乘，但是用了额外的 O(n) 空间

    Time: O(n)
    Extra Space: O(n)
    '''
    def productExceptSelf(self, nums):
        length = len(nums)

        order, reverse = [[1] * length for i in xrange(2)]
        for i in xrange(length):
            order[i] = (order[i - 1] if i > 0 else 1) * nums[i]
            reverse[length - 1 - i] = (
                reverse[length - i] if i > 0 else 1) * nums[length - 1 - i]

        return [(order[i - 1] if i > 0 else 1) *
                (reverse[i + 1] if i + 1 < length else 1)
                for i in xrange(length)]


class Solution(object):
    '''算法思路：

    遍历两边，第一遍从前往后，第二遍从后往前

    Time: O(n)
    Extra Space: (1)
    '''
    def productExceptSelf(self, nums):
        length, product, r = len(nums), 1, []
        for i in xrange(length):
            r.append(product)
            product *= nums[i]

        product = 1
        for i in xrange(length - 1, -1, -1):
            r[i] *= product
            product *= nums[i]

        return r


s = Solution()
print s.productExceptSelf([1, 2, 3, 4])
