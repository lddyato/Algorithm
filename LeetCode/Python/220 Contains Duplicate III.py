# -*- coding: utf-8 -*-

'''
Contains Duplicate III
======================

Given an array of integers, find out whether there are two distinct indices
i and j in the array such that the difference between nums[i] and nums[j] is
at most t and the difference between i and j is at most k.
'''


class Solution(object):
    '''算法思路：

    先满足 k，然后找满足 t 的

    Time 最差: O(n^2)
    结果：TLE
    '''
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums) and j - i <= k:
                if abs(nums[j] - nums[i]) <= t:
                    return True
                j += 1
            i += 1
        return False


class Solution(object):
    '''算法思路：

    先满足 t，然后找满足 k 的

    Time 最差: O(n^2)
    结果：AC

    其实这种算法和上面一样，只不过 leetcode 上的测试数据是针对上面的
    '''
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        nums = sorted(enumerate(nums), key=lambda x: x[1])

        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums) and nums[j][1] - nums[i][1] <= t:
                if abs(nums[j][0] - nums[i][0]) <= k:
                    return True
                j += 1
            i += 1
        return False


class Solution(object):
    '''算法思路：

    利用桶的思想，参考
    https://leetcode.com/discuss/48670/o-n-python-using-buckets-with-explanation-10-lines
    '''
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k <= 0:
            return False

        buckets = {}
        for i, v in enumerate(nums):
            bucketNum = v / (t + 1)
            for idx in xrange(bucketNum - 1, bucketNum + 2):
                if idx in buckets and abs(buckets[idx] - v) <= t:
                    return True

            buckets[bucketNum] = v

            if len(buckets) > k:
                del buckets[nums[i - k] / (t + 1)]

        return False


s = Solution()
print s.containsNearbyAlmostDuplicate([2, 1], 1, 1)
