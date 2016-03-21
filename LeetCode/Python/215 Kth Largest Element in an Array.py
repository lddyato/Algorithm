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
    def findKthLargest(self, nums, k):
        pivot, n = nums[0], len(nums)
        low, high = 0, n - 1

        while low < high:
            while low < n and nums[low] >= pivot:
                low += 1
            while high >= 0 and nums[high] < pivot:
                high -= 1

            if low > high:
                break
            nums[low], nums[high] = nums[high], nums[low]

        nums[0], nums[high] = nums[high], nums[0]

        if high + 1 < k:
            return self.findKthLargest(nums[high + 1:], k - high - 1)

        if high + 1 > k:
            return self.findKthLargest(nums[:high], k)

        return nums[high]


class Solution(object):
    '''算法思路：

    利用堆维护前 k 大，最后堆顶即为所求

    Time: O(k + n*log(k))
    '''
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            heapq.heappushpop(heap, nums[i])

        return heapq.heappop(heap)


class MaxHeap(object):
    def __init__(self, heap):
        self.heap = heap
        self.build()

    def heapify(self, start, end):
        father, heap = start, self.heap
        while 1:
            son = father * 2 + 1
            if son > end:
                break

            if son + 1 <= end and heap[son + 1] > heap[son]:
                son += 1

            if heap[son] > heap[father]:
                heap[son], heap[father] = heap[father], heap[son]

            father = son

    def build(self):
        n = len(self.heap)
        for start in range(n >> 1, -1, -1):
            self.heapify(start, n - 1)

    def push(self, num):
        self.heap.append(num)
        son, heap = len(self.heap) - 1, self.heap

        while 1:
            father = (son - 1) >> 1
            if father < 0:
                break

            if heap[son] > heap[father]:
                heap[son], heap[father] = heap[father], heap[son]

    def pop(self):
        top, tail = self.heap[0], self.heap.pop()
        if self.heap:
            self.heap[0] = tail
            self.heapify(0, len(self.heap) - 1)
        return top


class Solution(object):
    '''算法思路：

    先生成一个堆，然后 pop 第 k 个

    Time: O(n + k*log(n))
    '''
    def findKthLargest(self, nums, k):
        heap = MaxHeap(nums)
        for _ in range(k):
            r = heap.pop()
        return r


s = Solution()
print s.findKthLargest([7,6,5,4,3,2,1], 5)
