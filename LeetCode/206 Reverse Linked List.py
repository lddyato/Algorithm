# -*- coding: utf-8 -*-

'''
Reverse Linked List
===================

Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you
implement both?
'''


class Solution(object):
    '''算法思路：

    遍历, 即 iteratively
    '''
    def reverseList(self, head):
        current, pre, next = head, None, None
        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next
        return pre


class Solution(object):
    '''算法思路：同上

    与上面不同的是减少了无关变量
    '''

    def reverseList(self, head):
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev


class Solution(object):
    '''算法思路：

    递归
    '''
    def reverseList(self, head):
        def reverse(head, pre):
            if not head:
                return pre

            next = head.next
            head.next = pre

            return reverse(next, head)

        return reverse(head, None)
