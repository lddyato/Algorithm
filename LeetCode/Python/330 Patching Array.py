# -*- coding: utf-8 -*-

'''
Patching Array
==============

Given a sorted positive integer array nums and an integer n, add/patch elements
to the array such that any number in range [1, n] inclusive can be formed by
the sum of some elements in the array. Return the minimum number of patches
required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.

Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
[2,3], [1,2,3].

Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].

So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
'''


class Solution(object):
    """算法思路：

    maxReach 表示当前能够达到的最大值，每一步一定要尽可能地使maxReach更大,
    当 nums[i] > maxReach + 1 的时候，maxReach + 1 就会缺失，因为我们可以补上
    maxReach + 1, 这样 maxReach = maxReach * 2 + 1, 否则 maxReach += nums[i]

    参考了：https://leetcode.com/discuss/102653/c-8ms-greedy-solution-with-explanation
    """

    def minPatches(self, nums, n):
        maxReach, r, i = 0, 0, 0
        while maxReach < n:
            if i < len(nums) and nums[i] <= maxReach + 1:
                maxReach += nums[i]
                i += 1
            else:
                maxReach += maxReach + 1
                r += 1
        return r


s = Solution()
t print s.minPatches([], 8)
