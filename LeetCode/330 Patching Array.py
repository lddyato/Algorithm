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
    '''算法思路：

    miss 表示区间 [1, miss) 右边缘，当我们便利访问 nums 到 nums[i] 时，如果
    nums[i] <= miss，则从 [1, miss - 1] 我们加一个遍 nums[i]，能够到达的最右侧为
    miss - 1 + nums[i]，则我们期望达到的下一个值为 miss + nums[i]，一直这样直到
    miss > n.

    参考了：https://leetcode.com/discuss/82822/solution-explanation
    '''
    def minPatches(self, nums, n):
        miss, r, i, m = 1, 0, 0, len(nums)
        while miss <= n:
            if i < m and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                r += 1
        return r


s = Solution()
print s.minPatches([], 8)
