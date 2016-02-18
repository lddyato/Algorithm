# -*- coding: utf-8 -*-

'''
Convert Sorted List to Binary Search Tree
=========================================

Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''算法思路：

    每次从 root 查找并插入，这种做法不能保证结果是 height balanced BST

    结果：TLE
    '''
    def sortedListToBST(self, head):
        root = None
        while head:
            if not root:
                root = TreeNode(head.val)
            else:
                current = root
                while 1:
                    if head.val <= current.val:
                        if current.left:
                            current = current.left
                        else:
                            current.left = TreeNode(head.val)
                            break
                    else:
                        if current.right:
                            current = current.right
                        else:
                            current.right = TreeNode(head.val)
                            break

            head = head.next
        return root


class Solution(object):
    '''算法思路：

    每次以中间的 node 为 pivot，left，right 分别为左右两部分 root
    '''
    def sortedListToBST(self, head):
        if not head or not head.next:
            return head and TreeNode(head.val) or head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None

        root = TreeNode(slow.val)
        root.left, root.right = map(self.sortedListToBST, (head, slow.next))

        return root
