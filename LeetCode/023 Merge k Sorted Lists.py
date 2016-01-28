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
