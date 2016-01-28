# -*- coding: utf-8 -*-

'''
Search in Rotated Sorted Array II
=================================

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''


class Solution(object):
    '''算法思路：

    二分法查找 pivot 的同时，对不包含 pivot 的部分进行 binary_search target,
    不过需要注意的一点是：对于重复的部分需要略过，注意上限和下限
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
                    return True

        low, high = 0, len(nums) - 1
        while low <= high:
            while low + 1 < high and nums[low + 1] == nums[low]:
                low += 1

            while high - 1 > low and nums[high - 1] == nums[high]:
                high -= 1

            mid = (low + high) / 2
            if nums[mid] < nums[low]:
                r = binary_search(mid, high)
                if r:
                    return r

                high = mid - 1
            elif nums[mid] > nums[high]:
                r = binary_search(low, mid)
                if r:
                    return r

                low = mid + 1
            else:
                r = binary_search(low, high)
                if r:
                    return r

                break
        return False


s = Solution()
print s.search([3, 1, 1], 1)
