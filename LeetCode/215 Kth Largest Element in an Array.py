# -*- coding: utf-8 -*-

'''
Kth Largest Element in an Array
===============================

Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


class Solution(object):
    '''算法思路：

    先排序，然后返回第 k 个

    Time: O(n*log(n))
    '''
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]


class Solution(object):
    '''算法思路：

    类似于快排里边的交换，一直交换直到当前位置刚好是 k，效率要比上面方法高

    Time: O(n*log(n))
    '''
    def find(self, nums, k, start, end):
        i, j = start + 1, end

        while 1:
            while i <= end  and nums[i] >= nums[start]:
                i += 1
            while j > 0 and nums[j] < nums[start]:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[start], nums[j] = nums[j], nums[start]

        current = j - start + 1
        if k == current:
            return nums[j]

        return (
            self.find(nums, k - current, j + 1, end)
            if k > current else self.find(nums, k, start, j - 1)
        )

    def findKthLargest(self, nums, k):
        return self.find(nums, k, 0, len(nums) - 1)


s = Solution()
print s.findKthLargest([7,6,5,4,3,2,1], 5)
