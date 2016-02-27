# -*- coding: utf-8 -*-

'''
快排
===

时间复杂度：O(n * log(n))
空间复杂度：O(1)

是否稳定：否


twoWayPartition 和 threeWayPartition 的不同点在于：

- threeWayPartition 后的结果分为 3 部分，左边全部小于 pivot，中间全部等于 pivot,
  右边全部大于 pivot
- twoWayPartition 后的结果分为 2 部分，左半部分 <= pivot(混合排列)，右半部分 > pivot

一般用 twoWayPartition 的地方都可以用 threeWayPartition，但是用 threeWayPartition 的
地方不一定能够用 twoWayPartition，比如 LeetCode 第 75 题《Sort Colors》
'''


def quick_sort(array, start, end):
    '''
    two way partition
    '''
    if start >= end:
        return

    pivot, i, j = array[start], start + 1, end
    while 1:
        while i <= end and array[i] <= pivot:
            i += 1
        while j > start and array[j] > pivot:
            j -= 1
        if i > j:
            break
        array[i], array[j] = array[j], array[i]
    array[start], array[j] = array[j], array[start]

    quick_sort(array, start, j - 1)
    quick_sort(array, j + 1, end)

    return array


def quick_sort(nums, start, end):
    '''
    three way partition
    '''
    if start >= end:
        return

    pivot, low, high, i = nums[start], start, end, start
    while i <= high:
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        elif nums[i] > pivot:
            nums[high], nums[i] = nums[i], nums[high]
            high -= 1
        else:
            i += 1

    quick_sort(nums, start, high - 1)
    quick_sort(nums, high + 1, end)

    return nums


a = [23, 4, 5, 1, 345, 89, 7]
print quick_sort(a, 0, len(a) - 1)


# ========================================
# 扩展：求第 k 大
# ========================================


# twoWayPartition，迭代版本
def getKth(nums, start, end, k):
    start, end = 0, len(nums) - 1
    while 1:
        pivot, low, high = nums[start], start, end
        while 1:
            while low <= end and nums[low] <= pivot:
                low += 1
            while high >= 0 and nums[high] > pivot:
                high -= 1
            if low >= high:
                break
            nums[low], nums[high] = nums[high], nums[low]
        nums[start], nums[high] = nums[high], nums[start]

        if high - start + 1 == k:
            return nums[high]

        if high - start + 1 < k:
            start, k = high + 1, end, k - high + start - 1
        else:
            end = high - 1


# threeWayPartition，迭代版本
def getKth(nums, k):
    start, end = 0, len(nums) - 1
    while 1:
        pivot, low, high, i = nums[start], start, end, start
        while i <= high:
            if nums[i] < pivot:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
                i += 1
            elif nums[i] > pivot:
                nums[high], nums[i] = nums[i], nums[high]
                high -= 1
            else:
                i += 1

        if high - start + 1 == k:
            return nums[high]

        if high - start + 1 < k:
            start, k = high + 1, k - high + start - 1
        else:
            end = high - 1


import heapq

# heap 获得前 k 大
def getKth(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap
