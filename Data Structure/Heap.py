# -*- coding: utf-8 -*-

"""
堆
==

最小堆 & 最大堆: https://en.wikipedia.org/wiki/Heap_(data_structure)
"""

import operator


class _Heap(object):
    _compare = None

    def __init__(self, heap):
        self.heap = heap
        self.build()

    def heapify(self, start=0, end=None):
        father, heap, end = start, self.heap, end or len(self.heap)
        while 1:
            son = father * 2 + 1
            if son >= end:
                break

            if son + 1 < end and self._compare(heap[son + 1], heap[son]):
                son += 1

            if not self._compare(heap[son], heap[father]):
                break

            heap[son], heap[father] = heap[father], heap[son]
            father = son

    def build(self):
        for start in range(len(self.heap) >> 1, -1, -1):
            self.heapify(start)

    def push(self, item):
        self.heap.append(item)
        son, heap = len(self.heap) - 1, self.heap

        while 1:
            father = (son - 1) >> 1
            if father < 0 or not self._compare(heap[son], heap[father]):
                break

            heap[son], heap[father] = heap[father], heap[son]
            son = father

    def pop(self):
        top, tail = self.heap[0], self.heap.pop()
        if self.heap:
            self.heap[0] = tail
            self.heapify()
        return top

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.heap)

    def __getitem__(self, index):
        return self.heap[index]

    def __len__(self):
        return len(self.heap)

    def __nonzero__(self):
        return bool(self.heap)

    __bool__ = __nonzero__


class MinHeap(_Heap):
    _compare = operator.le


class MaxHeap(_Heap):
    _compare = operator.ge
