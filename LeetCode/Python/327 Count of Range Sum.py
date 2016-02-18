# -*- coding: utf-8 -*-

'''
Count of Range Sum
==================

Given an integer array nums, return the number of range sums that lie in
[lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices
i and j (i ≤ j), inclusive.

Note:
- A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.

The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are:
-2, -1, 2.
'''


class Solution(object):
    '''算法思路：

    计算前缀和，查看每个 range，看其是否符合要求

    Time: O(n^2)

    结果：TLE
    '''
    def countRangeSum(self, nums, lower, upper):
        sums = [0]
        [sums.append(sums[-1] + num) for num in nums]

        return sum([
            lower <= sums[j + 1] - sums[i] <= upper
            for i in xrange(len(nums)) for j in xrange(i, len(nums))
        ])


import bisect


class Solution(object):
    '''算法思路：

    分治法，对 nums 进行分治，详细说明可查考
    https://leetcode.com/discuss/79907/summary-divide-conquer-based-binary-indexed-based-solutions

    问题的关键在于找到问题的本质，其实就是找不同的 i, j 使得 S(i, j) 满足情况

    结果：AC
    '''
    def countRangeSum(self, nums, lower, upper):
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return int(lower <= nums[0] <= upper)

        mid = n >> 1
        count = sum([
            self.countRangeSum(array, lower, upper)
            for array in [nums[:mid], nums[mid:]]
        ])

        suffix, prefix = [0] * (mid + 1), [0] * (n - mid + 1)
        for i in xrange(mid - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in xrange(mid, n):
            prefix[i - mid + 1] = prefix[i - mid] + nums[i]

        suffix, prefix = suffix[:-1], sorted(prefix[1:])
        count += sum([
            bisect.bisect_right(prefix, upper - s) -
            bisect.bisect_left(prefix, lower - s)
            for s in suffix
        ])
        return count


class Solution(object):
    '''算法思路：

    分治法，对 prefix 进行分治

    结果：AC
    '''
    def merge(self, arr1, arr2):
        r, i, j = [], 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                r.append(arr1[i])
                i += 1
            else:
                r.append(arr2[j])
                j += 1
        r += arr1[i:] + arr2[j:]
        return r

    def count(self, prefix, start, end, lower, upper):
        if start >= end:
            return 0

        mid = start + (end - start + 1 >> 1)
        count = sum([
            self.count(prefix, s, e, lower, upper)
            for s, e in ((start, mid - 1), (mid, end))
        ])

        l, r = mid, mid
        for i in xrange(start, mid):
            while l <= end and prefix[l] - prefix[i] < lower:
                l += 1
            while r <= end and prefix[r] - prefix[i] <= upper:
                r += 1
            count += r - l

        prefix[start:end + 1] = self.merge(
            prefix[start:mid], prefix[mid:end + 1])

        return count

    def countRangeSum(self, nums, lower, upper):
        n = len(nums)

        prefix = [0] * (n + 1)
        for i, v in enumerate(nums, 1):
            prefix[i] = prefix[i - 1] + v

        return self.count(prefix, 0, n, lower, upper)


s = Solution()
print s.countRangeSum([-2, 5, -1], -2, 2)
