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

        current = head.next
        head.next = None

        while current:
            next = current.next

            pre, cursor = None, head
            while cursor and current.val > cursor.val:
                pre, cursor = cursor, cursor.next

            if pre:
                pre.next = current
                current.next = cursor
            else:
                current.next = head
                head = current

            current = next

        return head


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
