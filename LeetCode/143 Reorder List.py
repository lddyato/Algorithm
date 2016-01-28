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
        if not head:
            return

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        if slow and fast:
            slow = slow.next

        rev, cursor = None, slow
        while cursor:
            rev, rev.next, cursor = cursor, rev, cursor.next

        tail, current = None, head
        while current and current != slow:
            next = current.next

            if not tail:
                tail = current
            else:
                tail.next = current
                tail = current

            if rev:
                tail.next = rev
                tail = rev

                rev = rev.next

            current = next

        if tail:
            tail.next = None


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
