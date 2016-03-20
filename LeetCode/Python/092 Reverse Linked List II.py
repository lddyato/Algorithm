# -*- coding: utf-8 -*-

'''
Reverse Linked List II
======================

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    将整个列表分成三部分，对中间部分进行翻转
    '''
    def reverseBetween(self, head, m, n):
        firstHead = firstTail = ListNode(None)
        secondHead = secondTail = ListNode(None)

        revHead, revTail, i = None, None, 1
        while head:
            next = head.next

            if i < m:
                firstTail.next = firstTail = head
            elif i > n:
                secondTail.next = secondTail = head
            else:
                head.next, revHead = revHead, head
                if not revTail:
                    revTail = head

            head = next
            i += 1

        firstTail.next, revTail.next = revHead, secondHead.next
        return firstHead.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
head = s.reverseBetween(a, 2, 4)

while head:
    print head
    head = head.next
