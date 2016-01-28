# -*- coding: utf-8 -*-

'''
Sliding Window Maximum
======================

Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers
in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
- You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for
  non-empty array.

Follow up:
Could you solve it in linear time?
'''


class Solution(object):
    '''算法思路：

    每次寻找 K 个数字的最大值

    Time: O(n*k)
    '''
    def maxSlidingWindow(self, nums, k):
        return [
            max(nums[i:i + k])
            for i in xrange(len(nums) - k + 1)
        ] if nums else []


import collections


class Solution(object):
    '''算法思路：

    双端队列，保证队列是非递增数列，这样最大的总在第一位，然后每次把超过窗口的元素去掉

    Time: O(n)
    '''
    def maxSlidingWindow(self, nums, k):
        n, deque, r = len(nums), collections.deque(), []
        for i, v in enumerate(nums):
            while deque and deque[0] < i - k + 1:
                deque.popleft()

            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)

            if i >= k - 1:
                r.append(nums[deque[0]])
        return r


s = Solution()
print s.maxSlidingWindow([1, -1], 1)
