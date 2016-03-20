# -*- coding: utf-8 -*-

'''
Swap Nodes in Pairs
===================

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values
in the list, only nodes itself can be changed.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    成对的往结果列表里边 append
    '''
    def swapPairs(self, head):
        dummy = tail = ListNode(None)
        while head and head.next:
            next = head.next.next
            tail.next = tail = head.next
            tail.next = tail = head
            head = next

        if head:
            tail.next = tail = head

        tail.next = None
        return dummy.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

s = Solution()
print s.swapPairs(a)
