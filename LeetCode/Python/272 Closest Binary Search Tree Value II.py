# -*- coding: utf-8 -*-

'''
Closest Binary Search Tree Value II
===================================

Given a non-empty binary search tree and a target value, find k values in the
BST that are closest to the target.

Note:

- Given target value is a floating point.
- You may assume k is always valid, that is: k ≤ total nodes.
- You are guaranteed to have only one unique set of k values in the BST that
  are closest to the target.

Follow up:

Assume that the BST is balanced, could you solve it in less than O(n) runtime
(where n = total nodes)?
'''


import bisect


class Solution(object):
    '''算法思路：

    首先中序遍历整个树，得到序列后二分查找 target 的位置 i，从 i 处将序列分成两部分,
    然后将前半部分反转，归并排序得到前 k 个离 target 最近的序列，此序列从前往后依次离
    target 越来越远

    Time: O(n)
    '''
    def closestKValues(self, root, target, k):
        stack, queue = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                queue.append(root.val)
                root = root.right

        i = bisect.bisect(queue, target)
        i, j, n, r = i - 1, i, len(queue), []

        while i >= 0 and j < n and len(r) < k:
            if abs(queue[i] - target) < abs(queue[j] - target):
                r.append(queue[i])
                i -= 1
            else:
                r.append(queue[j])
                j += 1

        r += (queue[:i + 1][::-1] or queue[j:])[:k - len(r)]
        return r



class Solution(object):
    '''算法思路：

    在中序遍历的时候维护一个长度为 k 的 window，每次比较当前值和 window 头，依据是
    最后的结果序列一定是最 close 的在中心，越往后差距越大

    Time: O(n)
    '''
    def closestKValues(self, root, target, k):
        stack, queue = [], collections.deque()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()

                if len(queue) < k:
                    queue.append(root.val)
                elif abs(queue[0] - target) > abs(root.val - target):
                    queue.popleft()
                    queue.append(root.val)
                else:
                    break

                root = root.right
        return list(queue)



class Solution(object):
    '''算法思路：

    用两个栈分别表示前序和后序，然后每次比较从栈顶，然后把最近的那个放到结果中，然后依次
    找到前序的前序，和后序的后序

    Time: O(klog(n))
    '''
    def getPredecessor(self, node, predecessors):
        node = node.left
        while node:
            predecessors.append(node)
            node = node.right

    def getSuccessor(self, node, successors):
        node = node.right
        while node:
            successors.append(node)
            node = node.left

    def closestKValues(self, root, target, k):
        predecessors, successors, r = [], [], []
        while root:
            [predecessors, successors][target < root.val].append(root)
            root = [root.right, root.left][target < root.val]

        while len(r) < k:
            if not predecessors or (
                    successors and
                    successors[-1].val - target < target - predecessors[-1].val):
                node = successors.pop()
                r.append(node.val)
                self.getSuccessor(node, successors)
            else:
                node = predecessors.pop()
                r.append(node.val)
                self.getPredecessor(node, predecessors)
        return r


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(5)
a = TreeNode(2)
b = TreeNode(7)
c = TreeNode(0)
d = TreeNode(4)
e = TreeNode(6)
f = TreeNode(9)

root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f

s = Solution()
print s.closestKValues(root, 5.7, 5)
