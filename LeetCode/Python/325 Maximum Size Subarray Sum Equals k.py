# -*- coding: utf-8 -*-

'''
Maximum Size Subarray Sum Equals k
==================================

Given an array nums and a target value k, find the maximum length of a subarray
that sums to k. If there isn't one, return 0 instead.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
'''


class Solution(object):
    '''算法思路：

    在这里 sliding window 不再适用，sliding window 适用于具有单调性的队列
    '''
    def maxSubArrayLen(self, nums, k):
        record, sum, r = {}, 0, 0
        for i, num in enumerate(nums):
            sum += num

            if sum == k:
                r = i + 1
            elif sum - k in record:
                r = max(i - record[sum - k], r)

            if sum not in record:
                record[sum] = i

        return r


s = Solution()
print s.maxSubArrayLen([1, -1, 5, -2, 3], 3)
