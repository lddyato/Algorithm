# -*- coding: utf-8 -*-

'''
Remove Nth Node From End of List
================================

Given a linked list, remove the nth node from the end of list and return its
head.

For example,

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes
1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    快慢指针的变形
    '''
    def removeNthFromEnd(self, head, n):
        if not n:
            return head

        i, pre, dest, current = 0, None, None, head
        while current:
            i += 1

            if i - n >= 0:
                pre, dest = dest, dest and dest.next or head

            current = current.next

        if dest:
            if pre:
                pre.next = dest.next
            else:
                head = dest.next

        return head


a = ListNode(1)
b = ListNode(2)

a.next = b

s = Solution()
head = s.removeNthFromEnd(a, 2)

while head:
    print head
    head = head.next
