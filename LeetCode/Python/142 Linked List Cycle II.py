# -*- coding: utf-8 -*-

'''
Linked List Cycle II
====================

Given a linked list, return the node where the cycle begins. If there is no
cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    Floyd判圈算法(Floyd Cycle Detection Algorithm) 或者
    龟兔赛跑算法(Tortoise and Hare Algorithm)

    https://zh.wikipedia.org/wiki/Floyd%E5%88%A4%E5%9C%88%E7%AE%97%E6%B3%95

    其实也可以根据 方程式 解出从 head 到环入口节点的距离
    '''
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return slow


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = b

s = Solution()
head = s.detectCycle(a)
print head
