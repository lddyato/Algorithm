# -*- coding: utf-8 -*-

'''
堆排序
=====

时间复杂度：O(n*log(n))
空间复杂度：O(1)

是否稳定：否
'''


class MaxHeap(object):
    def __init__(self, heap=[]):
        # 为了使外部不会意外的改变 heap，应该取其 copy，但是这里为了不再生成多余的空间
        # 直接使用其引用
        self.heap = heap
        self.build()

    @property
    def size(self):
        return len(self.heap)

    def heapify(self, root=0, end=None):
        # Time: O(h)
        heap, end = self.heap, self.size - 1 if end is None else end
        while 1:
            child = 2 * root + 1
            if child > end:
                break

            if child + 1 <= end and heap[child + 1] > heap[child]:
                child += 1

            if heap[child] > heap[root]:
                heap[root], heap[child] = heap[child], heap[root]

            root = child

    def build(self):
        # Time: O(n)
        for root in xrange(self.size >> 1, -1, -1):
            self.heapify(root)

    def push(self, num):
        heap = self.heap
        heap.append(num)
        child = self.size - 1

        while 1:
            root = (child - 1) >> 1
            if root < 0 or heap[child] <= heap[root]:
                break

            heap[child], heap[root] = heap[root], heap[child]
            child = root

    def pop(self):
        if not self.heap:
            return

        top, self.heap[0] = self.heap[0], self.heap.pop()
        self.heapify()
        return top


def heap_sort(array):
    '''
    堆排序用最大堆会直观一点，分两步：
    - 建立最大堆，关键在于 heapify
    - 交换堆顶和堆尾，然后 heapify 除了堆尾的元素

    对于 heap_sort 来说，实现 build() 和 heapify() 足够了
    '''
    heap = MaxHeap(array)
    for tail in xrange(heap.size - 1, -1, -1):
        heap.heap[0], heap.heap[tail] = heap.heap[tail], heap.heap[0]
        heap.heapify(end=tail - 1)
    return heap.heap


print heap_sort([19, 1, 10, 14, 16, 4, 7, 9, 3, 2, 8, 5, 11, 10])
