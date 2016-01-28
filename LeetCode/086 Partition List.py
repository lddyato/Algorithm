# -*- coding: utf-8 -*-

'''
Partition List
==============

Given a linked list and a value x, partition it such that all nodes less than x
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    两个新 head，一个往后面 push less than x，一个往后面 push >= x 的 node，最后
    两个部分相 连接即可

    需要特别注意的一个地方是：push 时一定要将 node.next 置为 Node，不然有可能会出现
    死循环
    '''
    def addNode(self, head, tail, node):
        node.next = None

        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node

        return head, tail

    def partition(self, head, x):
        lessHead = lessTail = greaterHead = greaterTail = None

        while head:
            node, head = head, head.next

            if node.val < x:
                lessHead, lessTail = self.addNode(lessHead, lessTail, node)
            else:
                greaterHead, greaterTail = self.addNode(
                    greaterHead, greaterTail, node)

        if not lessHead:
            return greaterHead

        lessTail.next = greaterHead
        return lessHead


a = ListNode(2)
b = ListNode(3)
c = ListNode(1)

a.next = b
b.next = c

s = Solution()

head = s.partition(a, 2)
while head:
    print head
    head = head.next
