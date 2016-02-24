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

    Time: O(m + n)
    '''
    def merge(self, nums1, nums2):
        nums, i, j, m, n = [], 0, 0, len(nums1), len(nums2)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        nums += nums1[i:] or nums2[j:]
        return nums, m + n

    def findMedianSortedArrays(self, nums1, nums2):
        nums, n = self.merge(nums1, nums2)
        if n & 1:
            return nums[n/2]
        return (nums[n/2 - 1] + nums[n/2]) / 2.0


class Solution(object):
    '''算法思路：

    找第 k 大元素，2/k 必须不大于 nums1 的长度

    每次比较 nums1[2/k - 1] 和 nums2[2/k - 1],
    - nums1[2/k - 1] == nums2[2/k - 1], 说明第 k 大为 nums1[2/k - 1]
    - nums1[2/k - 1] < nums2[2/k - 1]，说明 nums1[:2/k] 全部小于第 k 大
    - nums1[2/k - 1] > nums2[2/k - 1]，说明 nums2[:2/k] 全部小于第 k 大

    每次去掉 2/k 个比第 k 大数小的数

    Time: O(logk) = O(log(m + n))
    '''
    def findKth(self, nums1, nums2, k):
        m, n = map(len, (nums1, nums2))
        if m > n:
            return self.findKth(nums2, nums1, k)

        if m == 0:
            return nums2[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        p1 = min(k >> 1, m)
        p2 = k - p1

        if nums1[p1 - 1] < nums2[p2 - 1]:
            return self.findKth(nums1[p1:], nums2, k - p1)

        if nums1[p1 - 1] > nums2[p2 - 1]:
            return self.findKth(nums1, nums2[p2:], k - p2)

        return nums1[p1 - 1]

    def findMedianSortedArrays(self, nums1, nums2):
        length = sum(map(len, (nums1, nums2)))
        half = length >> 1

        if length & 1:
            return self.findKth(nums1, nums2, half + 1)

        return (
            self.findKth(nums1, nums2, half) +
            self.findKth(nums1, nums2, half + 1)
        ) / 2.0


class Solution(object):
    '''算法思路：

    我们可以将其看作是 merge 得到前 k 项，对于假设 nums1[0..i] 包含在结果中，那么
    nums2[0..k-i-2] 也包含在结果中，那么必有

    nums1[i] < nums2[k-i-1] 和 nums2[k-i-2] < nums1[i+1]
    我们只需要找到满足上述条件的第一个 i 即可

    Time: O(log(min(m, n, k)))
    '''
    def get(self, nums, p):
        if p < 0:
            return float('-inf')

        if p >= len(nums):
            return float('inf')

        return nums[p]

    def meeting(self, nums1, nums2, p1, p2):
        return max(self.get(nums1, p1), self.get(nums2, p2)) <= min(
            self.get(nums1, p1 + 1), self.get(nums2, p2 + 1))

    def findKth(self, nums1, nums2, k):
        low, high = 0, min(k, len(nums1)) - 1
        while low <= high:
            p1 = low + high >> 1
            p2 = k - p1 - 2

            # if it's the first element in nums1 meeting
            # max(nums1[p], nums2[k-p-2]) <= min(nums1[p+1], nums2[k-p-1])
            if self.meeting(nums1, nums2, p1, p2) and (
                    p1 == 0 or not self.meeting(nums1, nums2, p1-1, p2+1)):
                return max(nums1[p1], self.get(nums2, p2))

            if self.get(nums2, p2) > self.get(nums1, p1 + 1):
                low = p1 + 1
            else:
                high = p1 - 1

        return nums2[k - 1]

    def findMedianSortedArrays(self, nums1, nums2):
        m, n = map(len, (nums1, nums2))
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        half = m + n >> 1

        if (m + n) & 1:
            return self.findKth(nums1, nums2, half + 1)

        return (
            self.findKth(nums1, nums2, half) +
            self.findKth(nums1, nums2, half + 1)
        ) / 2.0


s = Solution()
print s.findMedianSortedArrays([1], [])
