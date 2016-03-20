# -*- coding: utf-8 -*-

'''
Merge k Sorted Lists
====================

Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    递归解决，每次找到最小的那个 node，然后剩余的再继续 merge

    假设 lists 的长度为 n，所有 list 的元素总和为 k，那么时间复杂度为：k * n

    结果：TLE
    '''
    def find_min(self, lists):
        m, index = None, None
        for i, l in enumerate(lists):
            if m is None or l.val < m.val:
                m, index = l, i

        return index, m

    def mergeKLists(self, lists):
        lists = filter(None, lists)

        if not lists:
            return

        index, head = self.find_min(lists)
        lists[index] = head.next

        head.next = self.mergeKLists(lists)
        return head


class Solution(object):
    '''算法思路：

    同上，只不过改成了迭代

    结果：TLE
    '''
    def find_min(self, lists):
        m, index = None, None
        for i, l in enumerate(lists):
            if m is None or l.val < m.val:
                m, index = l, i

        return index, m

    def mergeKLists(self, lists):
        lists = filter(None, lists)

        head, tail = None, None
        while lists:
            index, m = self.find_min(lists)
            if not head:
                head = tail = m
            else:
                tail.next = m
                tail = m

            if m.next:
                lists[index] = m.next
            else:
                del lists[index]

        return head


class Solution(object):
    '''算法思路：

    首先按照每个链表的第一个 node 排序，然后每次 del d=lists[0]，然后用二分法找出
    d.next 在 lists 的位置，然后插入进去，如此循环，直到 lists 为空

    假设 lists 长度为 n，所有 list 的元素总和为 k，那么复杂度上限为:
    max(k * log(n), n * log(n))

    结果：AC
    '''
    def find(self, lists, node):
        low, high, mid = 0, len(lists) - 1, None
        while low <= high:
            mid = (low + high) / 2
            if node.val >= lists[mid].val:
                low = mid + 1
            else:
                if mid > 0 and node.val >= lists[mid - 1].val:
                    return mid
                high = mid - 1
        return low

    def mergeKLists(self, lists):
        lists = sorted(filter(None, lists), key=lambda l: l.val)

        head, tail = None, None
        while lists:
            m = lists[0]

            if not head:
                head = tail = m
            else:
                tail.next = m
                tail = m

            del lists[0]

            next = m.next
            if next:
                lists.insert(self.find(lists, next), next)

        return head


class Solution(object):
    '''算法思路：

    类似于 merge sort，利用分而治之的思想

    结果：AC
    '''
    def merge(self, l1, l2):
        dummy = tail = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, tail, l1 = l1, l1, l1.next
            else:
                tail.next, tail, l2 = l2, l2, l2.next

        tail.next = l1 or l2
        return dummy.next

    def mergeKLists(self, lists):
        n = len(lists)
        if n < 2:
            return lists[0] if lists else None

        if n == 2:
            return self.merge(*lists)

        mid = n >> 1
        return self.merge(*map(self.mergeKLists, (lists[:mid], lists[mid:])))


class MinHeap(object):
    def __init__(self, heap):
        self.heap = heap
        self.build()

    def heapify(self, root=0, end=None):
        heap = self.heap
        end = end or len(self.heap)

        father = root
        while 1:
            son = 2 * father + 1
            if son >= end:
                break

            if son + 1 < end and heap[son + 1].val < heap[son].val:
                son += 1

            if heap[son].val < heap[father].val:
                heap[father], heap[son] = heap[son], heap[father]

            father = son

    def build(self):
        for root in range(len(self.heap) >> 1, -1, -1):
            self.heapify(root)

    def push(self, node):
        heap = self.heap

        heap.append(node)
        son = len(heap) - 1

        while 1:
            father = (son - 1) >> 1
            if father < 0:
                break

            if heap[son].val < heap[father].val:
                heap[father], heap[son] = heap[son], heap[father]

            son = father

    def pop(self):
        top, tail = self.heap[0], self.heap.pop()
        if self.heap:
            self.heap[0] = tail
            self.heapify()
        return top

    def empty(self):
        return not bool(self.heap)


class Solution(object):
    '''算法思路：

    维护一个大小为 len(lists) 的堆，每次取最小值 append 到列表最后

    结果：AC
    '''
    def mergeKLists(self, lists):
        heap = MinHeap(filter(None, lists))
        dummy = tail = ListNode(None)

        while not heap.empty():
            tail.next = tail = heap.pop()
            if tail.next:
                heap.push(tail.next)

        tail.next = None
        return dummy.next


def make_list(l):
    head, tail = None, None
    for v in l:
        node = ListNode(v)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node

    return head


lists = map(make_list, [
    [-8, -7, -7, -5, 1, 1, 3, 4],
    [-2],
    [-10, -10, -7, 0, 1, 3],
    [2]
])

s = Solution()
head = s.mergeKLists(lists)

while head:
    print head
    head = head.next
