# -*- coding: utf-8 -*-

'''
Insertion Sort List
===================

Sort a linked list using insertion sort.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode> {}'.format(self.val)


class Solution(object):
    '''算法思路：

    插入排序的思想，只不过是从前往后遍历
    '''
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next, tail = head, head.next
        dummy.next.next = None

        while tail:
            pre, current, next = dummy, dummy.next, tail.next
            while current:
                if tail.val <= current.val:
                    pre.next, tail.next = tail, current
                    break
                pre, current = current, current.next
            else:
                pre.next, tail.next = tail, None
            tail = next

        return dummy.next


a = ListNode(5)
b = ListNode(3)
c = ListNode(8)
d = ListNode(7)
e = ListNode(100)
f = ListNode(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head = a

s = Solution()
head = s.insertionSortList(a)

while head:
    print head
    head = head.next
