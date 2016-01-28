# -*- coding: utf-8 -*-

'''
Rotate Array
============

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
[5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different
ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
'''


class Solution(object):
    '''算法思路：

    用一个临时数组保存前半部分，然后把后半部分 copy 到 nums 的开头，接着把临时数组
    copy 到 nums

    Time: O(n)
    Space: O(n - k)

    结果：AC
    '''
    def rotate(self, nums, k):
        if not nums:
            return

        if k <= 0:
            return

        n = len(nums)
        k %= n

        temporary = nums[:n - k]

        i, j = 0, n - k
        while j < n:
            nums[i] = nums[j]
            i += 1
            j += 1

        j = 0
        while j < len(temporary):
            nums[i] = temporary[j]
            i += 1
            j += 1


class Solution(object):
    '''算法思路：

    每次把 nums 里边每一个都右移，最后一个放到 nums[0]，如此循环 k 此

    Time: O(k * n)
    Space: O(1)

    结果：TLE
    '''
    def rotate(self, nums, k):
        if not nums:
            return

        if k <= 0:
            return

        n = len(nums)
        k %= n

        count = 0
        while count < k:
            count += 1

            i, last = n - 1, nums[-1]
            while i >= 1:
                nums[i] = nums[i - 1]
                i -= 1

            nums[0] = last


class Solution(object):
    '''算法思路：

    先分别把两个部分反转，然后把整个数组反转

    Time: O(n)
    Space: O(1)

    结果：AC
    '''
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        if not nums:
            return

        if k <= 0:
            return

        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)


s = Solution()
print s.rotate([1, 2, 3, 4, 5, 6, 7], 1)
