# -*- coding: utf-8 -*-

'''
Maximum Subarray
================

Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
'''


class Solution(object):
    '''算法思路：

    当 sum < 0 时，设置 sum = 0
    '''
    def maxSubArray(self, nums):
        s, largest = 0, float('-inf')
        for num in nums:
            s += num
            largest, s = max(largest, s), max(s, 0)
        return largest


class Solution(object):
    '''算法思路：

    dp，dp[i] 为以 nums[i] 结尾的 subarray 的最大 sum
    '''
    def maxSubArray(self, nums):
        dp, largest = 0, float('-inf')
        for i in xrange(len(nums)):
            dp = max(dp + nums[i], nums[i])
            largest = max(largest, dp)
        return largest


class Solution(object):
    '''算法思路：

    分治法，参考
    https://leetcode.com/discuss/60435/c-an-clear-o-n-divide-and-conquer-solution-with-comments
    '''
    def sub(self, start, end):
        if start == end:
            return [self.nums[start]] * 4

        mid = (start + end) / 2
        left, right = self.sub(start, mid), self.sub(mid + 1, end)

        mx = max(left[0], right[0], left[2] + right[1])
        lmx = max(left[1], left[3] + right[1])
        rmx = max(right[2], left[2] + right[3])
        sum = left[3] + right[3]

        return (mx, lmx, rmx, sum)

    def maxSubArray(self, nums):
        self.nums = nums
        return self.sub(0, len(nums) - 1)[0]


s = Solution()
print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
