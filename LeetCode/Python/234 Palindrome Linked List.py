# -*- coding: utf-8 -*-

'''
Palindrome Linked List
======================

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    - 找出 mid node，将链表分为 two part
    - 将 second part 反转，也可以在找 mid node 的同时反转 first part
    - 比较这两个 part

    启发点：找出 mid node 时可以用 快慢 两个指针
    '''
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        slow, rev = fast and slow.next or slow, None
        while slow:
            rev, rev.next, slow = slow, rev, slow.next

        while rev and rev.val == head.val:
            rev, head = rev.next, head.next

        return not rev


class Solution(object):
    '''算法思路：

    找出 mid node 的同时，反转 first part，
    '''
    def isPalindrome(self, head):
        rev, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        slow = fast and slow.next or slow
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next

        return not rev


a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

s = Solution()
print s.isPalindrome(a)
