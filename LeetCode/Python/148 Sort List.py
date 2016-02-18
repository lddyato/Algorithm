# -*- coding: utf-8 -*-

'''
Sort List
=========

Sort a linked list in O(n log n) time using constant space complexity.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode> {}'.format(self.val)


class Solution(object):
    '''算法思路：

    快排，但是最坏的情况是 O(n^2)，所以本题 TLE 了

    结果：TLE
    '''
    def _sortList(self, head):
        if not head or not head.next:
            return head, head

        left = left_tail = ListNode(None)
        right = right_tail = ListNode(None)

        current = head.next
        while current:
            if current.val < head.val:
                left_tail.next, left_tail = current, current
            else:
                right_tail.next, right_tail = current, current

            current = current.next

        left_tail.next = right_tail.next = None

        left, left_tail = self._sortList(left.next)
        right, right_tail = self._sortList(right.next)

        if left:
            left_tail.next = head
        else:
            left = head

        head.next = right
        return left, right_tail or head

    def sortList(self, head):
        head, _ = self._sortList(head)
        return head


class Solution(object):
    '''算法思路：

    归并排序，稳定 O(n * log(n))

    结果：AC
    '''
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))


a = ListNode(3)
b = ListNode(2)
c = ListNode(1)

a.next = b
b.next = c

s = Solution()
head = s.sortList(a)

while head:
    print head
    head = head.next
