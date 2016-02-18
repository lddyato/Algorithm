# -*- coding: utf-8 -*-

'''
Delete Node in a Linked List
============================

Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node
with value 3, the linked list should become 1 -> 2 -> 4 after calling your
function.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    把数值前移，并把最后一个删除
    '''
    def deleteNode(self, node):
        pre = None
        while node.next:
            node.val = node.next.val
            pre, node = node, node.next
        pre.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d

s = Solution()
s.deleteNode(a)

head = a
while head:
    print head
    head = head.next
