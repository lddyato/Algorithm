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

    递归解决归并排序
    '''
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        if l1.val == l2.val:
            next = l1.next

            head = tail = l1
            tail.next = l2
            tail = l2

            l1, l2 = next, l2.next

        elif l1.val < l2.val:
            head = tail = l1
            l1 = l1.next
        else:
            head = tail = l2
            l2 = l2.next

        tail.next = self.mergeTwoLists(l1, l2)
        return head


class Solution(object):
    '''算法思路：

    迭代解决归并排序
    '''
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        head = tail = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, tail = l1, l1
                l1 = l1.next
            else:
                tail.next, tail = l2, l2
                l2 = l2.next

        tail.next = l1 or l2
        return head.next


class Solution(object):
    '''算法思路：

    迭代的另外一种写法
    '''
    def mergeTwoLists(self, l1, l2):
        head = tail = ListNode(None)
        while l1 or l2:
            if not l1 or not l2:
                l = l1 or l2
                tail.next = l

                return head

            while l1 and l2 and l1.val <= l2.val:
                tail.next, tail = l1, l1
                l1 = l1.next

            while l1 and l2 and l2.val <= l1.val:
                tail.next, tail = l2, l2
                l2 = l2.next

        return head.next


a = ListNode(1)
b = ListNode(1)

s = Solution()
head = s.mergeTwoLists(a, b)

while head:
    print head
    head = head.next
