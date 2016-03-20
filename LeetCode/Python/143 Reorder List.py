# -*- coding: utf-8 -*-

'''
Reorder List
============

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    通过快慢指针找到中间 node，然后将后半部分反转，最后将两个 part merge 起来
    '''
    def reorderList(self, head):
        if not (head and head.next):
            return

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        if fast:
            pre, slow = slow, slow.next

        if pre:
            pre.next = None

        rev = None
        while slow:
            rev, rev.next, slow = slow, rev, slow.next

        tail, current = None, head
        while rev:
            next = current.next
            if tail:
                tail.next = current
            current.next, tail, rev, current = rev, rev, rev.next, next

        if current:
            tail.next = current


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

s = Solution()
head = s.reorderList(a)

while head:
    print head
    head = head.next
