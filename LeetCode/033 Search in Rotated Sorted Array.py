# -*- coding: utf-8 -*-

'''
Search in Rotated Sorted Array
==============================

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.
'''


class Solution(object):
    '''算法思路：

    二分法查找 pivot 的同时，对不包含 pivot 的部分进行 binary_search target
    '''
    def search(self, nums, target):
        def binary_search(low, high):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    return mid
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] < nums[low]:
                r = binary_search(mid, high)
                if r != -1:
                    return r

                high = mid - 1
            elif nums[mid] > nums[high]:
                r = binary_search(low, mid)
                if r != -1:
                    return r

                low = mid + 1
            else:
                r = binary_search(low, high)
                if r != -1:
                    return r

                break
        return -1


s = Solution()
print s.search([4, 5, 6, 7, 8, 0, 1, 2, 3], 1)
