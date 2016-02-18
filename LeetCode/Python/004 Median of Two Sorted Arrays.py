# -*- coding: utf-8 -*-

'''
Median of Two Sorted Arrays
===========================

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).
'''


class Solution(object):
    '''算法思路：

    merge sort 成一个数组，然后取中位数，可以优化成取 第k大 值

    Time: O(n)
    '''
    def findMedianSortedArrays(self, nums1, nums2):
        i, j, len_1, len_2, nums = 0, 0, len(nums1), len(nums2), []

        while not (i >= len_1 and j >= len_2):
            if i < len_1:
                while j < len_2 and nums2[j] <= nums1[i]:
                    nums.append(nums2[j])
                    j += 1
            else:
                nums += nums2[j:]
                j = len_2

            if j < len_2:
                while i < len_1 and nums1[i] <= nums2[j]:
                    nums.append(nums1[i])
                    i += 1
            else:
                nums += nums1[i:]
                i = len_1

        return (nums[(len_1 + len_2 - 1) / 2] + nums[(len_1 + len_2) / 2]) / 2.0


class Solution(object):
    '''算法思路：

    https://leetcode.com/discuss/41621/very-concise-iterative-solution-with-detailed-explanation

    Time: O(log(min(M,N)))
    '''
    def findMedianSortedArrays(self, nums1, nums2):
        (len_1, len_2), (MIN, MAX) = map(
            len, (nums1, nums2)), map(float, ('-inf', 'inf'))

        if len_1 < len_2:
            return self.findMedianSortedArrays(nums2, nums1)

        low, high = 0, len_2 * 2
        while low <= high:
            C2 = (low + high) / 2
            C1 = len_1 + len_2 - C2

            L1 = nums1[(C1-1) / 2] if C1 > 0 else MIN
            L2 = nums2[(C2-1) / 2] if C2 > 0 else MIN
            R1 = nums1[C1 / 2] if C1 != 2 * len_1 else MAX
            R2 = nums2[C2 / 2] if C2 != 2 * len_2 else MAX

            if L1 > R2:
                low = C2 + 1
            elif L2 > R1:
                high = C2 - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0


s = Solution()
print s.findMedianSortedArrays([1], [])
