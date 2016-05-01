# -*- coding: utf-8 -*-

'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is
  the array's size.
'''


import collections


class Heap(object):
    def __init__(self):
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def heapify(self, start, end):
        father, heap = start, self.heap
        while 1:
            son = father * 2 + 1
            if son > end:
                break

            if son + 1 <= end and heap[son + 1][0] < heap[son][0]:
                son += 1

            if heap[son][0] < heap[father][0]:
                heap[father], heap[son] = heap[son], heap[father]

            father = son

    def build(self):
        for start in xrange(self.size >> 1, -1, -1):
            self.heapify(start, self.size - 1)

    def push(self, item):
        heap = self.heap
        heap.append(item)

        son = self.size - 1
        while 1:
            father = son - 1 >> 1
            if father < 0:
                break

            if heap[son][0] < heap[father][0]:
                heap[son], heap[father] = heap[father], heap[son]

            son = father

    def pop(self):
        if not self.heap:
            return

        top, tail = self.heap[0], self.heap.pop()
        if self.heap:
            self.heap[0] = tail

        self.heapify(0, self.size - 1)
        return top


class Solution(object):
    '''算法思路：

    维护频率组成的 Heap

    Time: O(max(n, (n - k) * log(k)))
    '''
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)

        heap = Heap()
        for key, val in counter.items():
            heap.push([val, key])
            if heap.size > k:
                heap.pop()

        return [heap.pop()[1] for _ in xrange(k)][::-1]


'========================================================================='


import heapq


class Pair(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __cmp__(self, other):
        return cmp(self.key, other.key)


class Solution(object):
    '''算法思路：

    同上，不过不是自己实现 heap，而是用了内建库

    Time: O(max(n, (n - k) * log(k)))
    '''
    def topKFrequent(self, nums, k):
        counter = [
            Pair(val, key) for key, val in collections.Counter(nums).items()
        ]

        heap = counter[:k]
        heapq.heapify(heap)

        for i in xrange(k, len(counter)):
            heapq.heappushpop(heap, counter[i])

        return [heapq.heappop(heap).val for _ in xrange(k)][::-1]


s = Solution()
print s.topKFrequent([1,1,1,2,2,3], 2)
