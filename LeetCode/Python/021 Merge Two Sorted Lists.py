# -*- coding: utf-8 -*-

'''
Merge Two Sorted Lists
======================

Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    迭代解决归并排序
    '''
    def mergeTwoLists(self, l1, l2):
        dummy = tail = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, tail, l1 = l1, l1, l1.next
            else:
                tail.next, tail, l2 = l2, l2, l2.next
        tail.next = l1 or l2
        return dummy.next


a = ListNode(1)
b = ListNode(1)

s = Solution()
head = s.mergeTwoLists(a, b)

while head:
    print head
    head = head.next
