# -*- coding: utf-8 -*-

'''
Odd Even Linked List
====================

Given a singly linked list, group all odd nodes together followed by the even
nodes. Please note here we are talking about the node number and not the value
in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
- The relative order inside both the even and odd groups should remain as it
  was in the input.
- The first node is considered odd, the second node even and so on ...
'''


class Solution(object):
    '''算法思路：

    用两个指针分别把奇偶串起来，然后连接起来即可
    '''
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        oddHead, oddTail, evenHead, evenTail, pre = (
            head, head, head.next, head.next, None)

        while oddTail and oddTail.next:
            next = oddTail.next

            oddTail.next = next.next
            pre, oddTail = oddTail, next.next

            evenTail.next = next
            evenTail = next

        evenTail.next = None
        if oddTail:
            oddTail.next = evenHead
        else:
            pre.next = evenHead

        return oddHead


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


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
head = s.oddEvenList(a)

while head:
    print head,
    head = head.next
