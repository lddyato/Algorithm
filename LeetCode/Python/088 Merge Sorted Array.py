# -*- coding: utf-8 -*-

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

Note:

You may assume that nums1 has enough space (size that is greater or equal to
m + n) to hold additional elements from nums2. The number of elements
initialized in nums1 and nums2 are m and n respectively.
'''


class Solution(object):
    '''算法思路：

    two pointers，当 nums1 中的 pointer 指的值大于 nums2 中 pointer 指的值时，
    把 nums1 指针后边的项往后移动后，把 nums2 对应的项赋值给 num1

    Time: O(n^2)
    '''
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0

        while j < n and i < m + n:
            if i - j >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                for k in range(m + j, i, -1):
                    nums1[k] = nums1[k - 1]

                nums1[i] = nums2[j]
                j += 1


class Solution(object):
    '''算法思路：

    由于 nums1 后面有足够的空间，因此可以从最后面比较，把大的放到 num1 的后面

    参考了：https://leetcode.com/discuss/8233/this-is-my-ac-code-may-help-you

    Time: O(n)
    '''
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]


s = Solution()
s.merge([1, 3, 5, 0, 0, 0, 0, 0, 0], 3, [-2, -1, 6], 3)
