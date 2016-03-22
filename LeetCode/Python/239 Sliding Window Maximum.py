# -*- coding: utf-8 -*-

'''
Sliding Window Maximum
======================

Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers
in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
- You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for
  non-empty array.

Follow up:
Could you solve it in linear time?
'''


class Solution(object):
    '''算法思路：

    每次寻找 K 个数字的最大值

    Time: O(n*k)
    '''
    def maxSlidingWindow(self, nums, k):
        return [
            max(nums[i:i + k])
            for i in xrange(len(nums) - k + 1)
        ] if nums else []


class MaxHeap(object):
    def __init__(self, heap):
        self.heap = heap
        self.build()

    def heapify(self, start, end):
        heap, father = self.heap, start
        while 1:
            son = 2 * father + 1
            if son > end:
                break

            if son + 1 <= end and heap[son + 1][0] > heap[son][0]:
                son += 1

            heap[father], heap[son] = heap[son], heap[father]
            father = son

    def build(self):
        for start in range(len(self.heap) >> 1, -1, -1):
            self.heapify(start, len(self.heap) - 1)

    def push(self, pair):
        self.heap.append(pair)
        son, heap = len(self.heap) - 1, self.heap

        while 1:
            father = (son - 1) >> 1
            if father < 0 or heap[son][0] <= heap[father][0]:
                break

            heap[father], heap[son] = heap[son], heap[father]
            son = father

    def pop(self):
        top, tail = self.heap[0], self.heap.pop()
        if self.heap:
            self.heap[0] = tail
            self.heapify(0, len(self.heap) - 1)
        return top

    def __getitem__(self, index):
        return self.heap[index]

    def __nonzero__(self):
        return bool(self.heap)


class Solution(object):
    '''算法思路：

    利用堆，每次去除不在窗口内的元素，然后找出栈顶元素

    Time: O(n*log(n))
    '''
    def maxSlidingWindow(self, nums, k):
        heap, r = MaxHeap([]), []
        for i, num in enumerate(nums):
            while heap and heap[0][1] < i - k + 1:
                heap.pop()
            heap.push([num, i])

            if i >= k - 1:
                r.append(heap[0][0])
        return r


import collections


class Solution(object):
    '''算法思路：

    双端队列，保证队列是非递增数列，这样最大的总在第一位，然后每次把超过窗口的元素去掉

    Time: O(n)
    '''
    def maxSlidingWindow(self, nums, k):
        deque, r = collections.deque(), []
        for i, num in enumerate(nums):
            while deque and deque[0][1] <= i - k:
                deque.popleft()

            while deque and num > deque[-1][0]:
                deque.pop()

            deque.append([num, i])

            if i >= k - 1:
                r.append(deque[0][0])
        return r


s = Solution()
print s.maxSlidingWindow([1, -1], 1)
