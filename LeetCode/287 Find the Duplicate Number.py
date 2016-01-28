# -*- coding: utf-8 -*-

'''
Find the Duplicate Number
=========================

Given an array nums containing n + 1 integers where each integer is between 1
and n (inclusive), prove that at least one duplicate number must exist. Assume
that there is only one duplicate number, find the duplicate one.

Note:
- You must not modify the array (assume the array is read only).
- You must use only constant, O(1) extra space.
- Your runtime complexity should be less than O(n^2).
- There is only one duplicate number in the array, but it could be repeated
  more than once.
'''


class Solution(object):
    '''算法思路：

    每个都比较一下，复杂度为 O(n^2)，果然 TLE

    结果：TLE
    '''
    def findDuplicate(self, nums):
        i, length = 0, len(nums)
        while i < length - 1:
            j = i + 1
            while j < length:
                if nums[j] == nums[i]:
                    return nums[j]
                j += 1
            i += 1


class Solution(object):
    '''算法思路：

    这里利用了一个事实：
    [1, n] 里边如果中间数 (1+n)/2 小的数的个数 count <= 中间数，那么重复的元素一定
    不在 1 到 (1+n)/2 之间

    Time: O(n * log(n))

    结果：AC
    '''
    def findDuplicate(self, nums):
        low, high = 1, len(nums) - 1
        while low < high:
            count, mid = 0, (low + high) / 2
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low


class Solution(object):
    '''算法思路：

    理论上来说，如果把 1 到 n 分别放到数组 index 分别为为 i - n 的位置上，那么最后只
    要判断 index 上的值的个数，就可以找到重复的数。

    照这个思路，从 index=0 (假设值为 v0) 处出发，一直把当前的数放到值所对应的 index
    上，如果没有重复的数，那么最后刚好会把所有的 v 放到 index=v 上。否则，会出现
    index=v 上已经被赋值，这时候就可以判断 v 为重复数

    Time: O(n)

    结果：AC

    这个方法更改了数组，不符合题意，只是为下一个解法做铺垫
    '''

    def findDuplicate(self, nums):
        current = nums[0]
        while current != nums[current]:
            next = nums[current]
            nums[current] = current
            current = next
        return current


class Solution(object):
    '''算法思路：

    接着上个 Solution 的思路，从上面可以看出，如果遇到 index=v 上已经被赋值，继续走
    下去会形成一个环，跟这一题很类似 《Linked List Cycle II》，链接：
    https://leetcode.com/problems/linked-list-cycle-ii/

    于是可以用 Floyd 判圈算法来做。

    这里有一篇专门介绍这个的文章：
    http://keithschwarz.com/interesting/code/?dir=find-duplicate

    Time: O(n)

    结果：AC
    '''
    def findDuplicate(self, nums):
        low = fast = nums[0]
        while 1:
            low, fast = nums[low], nums[nums[fast]]
            if low == fast:
                break

        low = nums[0]
        while low != fast:
            low, fast = nums[low], nums[fast]

        return low


s = Solution()
print s.findDuplicate([1, 2, 1])
