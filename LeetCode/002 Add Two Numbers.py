# -*- coding: utf-8 -*-

'''
Add Two Numbers
===============

You are given two linked lists representing two non-negative numbers. The
digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    2 -> 4 -> 3 的 reverse 是 3 -> 4 -> 2 也就是说实际数字是 342，同理
    5 -> 6 -> 4 为 465，理解了这一点就好做了
    '''
    def reverseList(self, head):
        rev = None

        while head:
            rev, rev.next, head = head, rev, head.next

        return rev

    def addNode(self, head, tail, value):
        node = ListNode(value)

        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node

        return head, tail

    def addTwoNumbers(self, l1, l2):
        div, rHead, rTail = 0, None, None
        while l1 or l2:
            v1, v2 = l1 and l1.val or 0, l2 and l2.val or 0

            div, mod = divmod(v1 + v2 + div, 10)
            rHead, rTail = self.addNode(rHead, rTail, mod)

            l1, l2 = l1 and l1.next, l2 and l2.next

        if div:
            rHead, _ = self.addNode(rHead, rTail, div)

        return rHead


s = Solution()

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)

d.next = e
e.next = f


r = s.addTwoNumbers(a, d)
while r:
    print r
    r = r.next
