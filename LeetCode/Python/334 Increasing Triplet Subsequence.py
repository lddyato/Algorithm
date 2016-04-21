# -*- coding: utf-8 -*-

'''
Given an unsorted array return whether an increasing subsequence of length 3
exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
'''


class Solution(object):
    '''算法思路：

    以每个数字为中心，找到左边最小的和右边最大的，如果满足 left < current < right,
    则存在

    Time: O(n)
    Space: O(n)
    '''
    def increasingTriplet(self, nums):
        n = len(nums)

        left, right = [0] * n, [0] * n

        minNum = float('inf')
        for i, num in enumerate(nums):
            minNum = min(num, minNum)
            left[i] = minNum

        maxNum = float('-inf')
        for i in range(n - 1, -1, -1):
            maxNum = max(nums[i], maxNum)
            right[i] = maxNum

        for i in range(1, n - 1):
            if left[i - 1] < nums[i] < right[i + 1]:
                return True
        return False


class Solution(object):
    '''算法思路：

    维护两个变量，使得 first < second，并且尽可能使 first, second 小，如果
    num > second，则说明存在

    当找到存在时，first，second 并不一定满足 first < second，比如 [10, 20, 1, 100]，
    但是依旧可以推出结果的正确性

    可以用归纳法证明算法的正确性, 过程有点类似于DFA
    '''
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


s = Solution()
print s.increasingTriplet([10, 20, 1, 100])
