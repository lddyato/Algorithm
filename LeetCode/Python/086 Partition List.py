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

    注意哑节点的技巧
    '''
    def partition(self, head, x):
        dummyLHead = dummyLTail = ListNode(0)
        dummyGHead = dummyGTail = ListNode(0)

        while head:
            if head.val < x:
                dummyLTail.next, dummyLTail = head, head
            else:
                dummyGTail.next, dummyGTail = head, head
            head = head.next

        dummyLTail.next, dummyGTail.next = dummyGHead.next, None
        return dummyLHead.next


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
