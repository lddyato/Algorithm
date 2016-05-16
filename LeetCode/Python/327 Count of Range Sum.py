# -*- coding: utf-8 -*-

'''
Count of Range Sum
==================

Given an integer array nums, return the number of range sums that lie in
[lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices
i and j (i ≤ j), inclusive.

Note:
- A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.

The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are:
-2, -1, 2.
'''


class Solution(object):
    '''算法思路：

    计算前缀和，查看每个 range，看其是否符合要求

    Time: O(n^2)

    结果：TLE
    '''
    def countRangeSum(self, nums, lower, upper):
        sums = [0]
        [sums.append(sums[-1] + num) for num in nums]

        return sum([
            lower <= sums[j + 1] - sums[i] <= upper
            for i in xrange(len(nums)) for j in xrange(i, len(nums))
        ])


'=========================================================================='


import random


class TreapNode(object):
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.countSum = 1
        self.left = None
        self.right = None
        self.priority = random.random()


class Treap(object):
    def __init__(self):
        self.root = None

    def getCountSum(self, root):
        return root and root.countSum or 0

    def rotateLeft(self, root):
        right = root.right
        right.countSum, root.countSum = root.countSum, sum(
            map(self.getCountSum, (root.left, right.left))) + root.count

        root.right = right.left
        right.left = root
        return right

    def rotateRight(self, root):
        left = root.left
        left.countSum, root.countSum = root.countSum, sum(
            map(self.getCountSum, (root.right, left.right))) + root.count

        root.left = left.right
        left.right = root
        return left

    def insertTo(self, root, key):
        if not root:
            return TreapNode(key)

        if key == root.key:
            root.count += 1
            root.countSum += 1
            return root

        if key < root.key:
            root.left = self.insertTo(root.left, key)
            if root.left.priority < root.priority:
                root = self.rotateRight(root)
        else:
            root.right = self.insertTo(root.right, key)
            if root.right.priority < root.priority:
                root = self.rotateLeft(root)

        root.countSum = sum(
            map(self.getCountSum, (root.left, root.right))) + root.count

        return root

    def insert(self, key):
        self.root = self.insertTo(self.root, key)

    def queryFrom(self, root, key):
        if not root:
            return 0

        if key < root.key:
            return self.queryFrom(root.left, key)

        return self.getCountSum(
            root.left) + root.count + self.queryFrom(root.right, key)

    def query(self, key):
        return self.queryFrom(self.root, key)


class Solution(object):
    '''算法思路：

    平衡二叉搜索树，这里用 Treap 实现，每次统计位于 [lower, upper] 中的和的个数
    '''
    def countRangeSum(self, nums, lower, upper):
        tree = Treap()

        s, r = 0, 0
        for num in nums:
            s += num
            r += tree.query(s - lower) - tree.query(s - upper - 1) + (
                lower <= s <= upper)
            tree.insert(s)

        return r


'===================================================================='


class RedBlackTreeNode(object):
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.countSum = 1
        self.left = None
        self.right = None
        self.isRed = True


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def getCountSum(self, root):
        return root and root.countSum or 0

    def rotateLeft(self, root):
        right = root.right

        right.countSum, root.countSum = root.countSum, sum(
            map(self.getCountSum, (root.left, right.left))) + root.count
        root.isRed, right.isRed = right.isRed, root.isRed

        root.right = right.left
        right.left = root
        return right

    def rotateRight(self, root):
        left = root.left

        left.countSum, root.countSum = root.countSum, sum(
            map(self.getCountSum, (root.right, left.right))) + root.count
        root.isRed, left.isRed = left.isRed, root.isRed

        root.left = left.right
        left.right = root
        return left

    def flipColor(self, root):
        root.isRed = not root.isRed
        root.left.isRed = not root.left.isRed
        root.right.isRed = not root.right.isRed
        return root

    def fix(self, root):
        if root.right and root.right.isRed:
            root = self.rotateLeft(root)

        if (root.left and root.left.isRed and
                root.left.left and root.left.left.isRed):
            root = self.rotateRight(root)

        if root.left and root.left.isRed and root.right and root.right.isRed:
            root = self.flipColor(root)

        root.countSum = sum(
            map(self.getCountSum, (root.left, root.right))) + root.count

        return root

    def insertTo(self, root, key):
        if not root:
            return RedBlackTreeNode(key)

        if key == root.key:
            root.count += 1
            root.countSum += 1
            return root

        if key < root.key:
            root.left = self.insertTo(root.left, key)
        else:
            root.right = self.insertTo(root.right, key)

        return self.fix(root)

    def insert(self, key):
        self.root = self.insertTo(self.root, key)
        self.root.isRed = False

    def queryFrom(self, root, key):
        if not root:
            return 0

        if key < root.key:
            return self.queryFrom(root.left, key)

        return self.getCountSum(
            root.left) + root.count + self.queryFrom(root.right, key)

    def query(self, key):
        return self.queryFrom(self.root, key)


class Solution(object):
    '''算法思路：

    同上，只不过这里用 红黑树 实现
    '''
    def countRangeSum(self, nums, lower, upper):
        tree = RedBlackTree()

        s, r = 0, 0
        for num in nums:
            s += num
            r += tree.query(s - lower) - tree.query(s - upper - 1) + (
                lower <= s <= upper)
            tree.insert(s)

        return r


'=================================================================='


import bisect


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.BIT = [0] * (n + 1)

    def update(self, index):
        i = index + 1
        while i < len(self.BIT):
            self.BIT[i] += 1
            i += i & (-i)

    def query(self, index):
        i, r = index + 1, 0
        while i >= 1:
            r += self.BIT[i]
            i -= i & (-i)
        return r


class Solution(object):
    '''算法思路：

    树状数组，用 BinaryIndexedTree 用来存储 f(prefix_sum) 出现的次数，然后统计即可

    关键点在于在 prefix_sum 和 BIT 下表之间的映射
      - 如果用 prefix_sum 直接来做 BIT 下标，那么当 prefix_sum 很大的时候，会占用非常大
        的内存
      - 用映射函数 y = f(prefix_sum)，使得 f 单调递增，prefix_sum 为前缀和，y 为 BIT
        的下标
    '''
    def countRangeSum(self, nums, lower, upper):
        sums = [0] * len(nums)
        for i, num in enumerate(nums):
            sums[i] = sums[i - 1] + num

        sortedSums = sorted(set(sums))
        table = {v: i for i, v in enumerate(sortedSums)}

        tree, r = BinaryIndexedTree(len(table)), 0
        for s in sums:
            r += tree.query(
                bisect.bisect_right(sortedSums, s - lower) - 1) - tree.query(
                bisect.bisect_right(sortedSums, s - upper - 1) - 1) + (
                lower <= s <= upper)
            tree.update(table[s])

        return r


'========================================================================'


import bisect


class Solution(object):
    '''算法思路：

    分治法，对 nums 进行分治，详细说明可查考
    https://leetcode.com/discuss/79907/summary-divide-conquer-based-binary-indexed-based-solutions

    问题的关键在于找到问题的本质，其实就是找不同的 i, j 使得 S(i, j) 满足情况

    结果：AC
    '''
    def countRangeSum(self, nums, lower, upper):
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return int(lower <= nums[0] <= upper)

        mid = n >> 1
        count = sum([
            self.countRangeSum(array, lower, upper)
            for array in [nums[:mid], nums[mid:]]
        ])

        suffix, prefix = [0] * (mid + 1), [0] * (n - mid + 1)
        for i in xrange(mid - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in xrange(mid, n):
            prefix[i - mid + 1] = prefix[i - mid] + nums[i]

        suffix, prefix = suffix[:-1], sorted(prefix[1:])
        count += sum([
            bisect.bisect_right(prefix, upper - s) -
            bisect.bisect_left(prefix, lower - s)
            for s in suffix
        ])
        return count


class Solution(object):
    '''算法思路：

    分治法，对 prefix 进行分治

    结果：AC
    '''
    def merge(self, arr1, arr2):
        r, i, j = [], 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                r.append(arr1[i])
                i += 1
            else:
                r.append(arr2[j])
                j += 1
        r += arr1[i:] + arr2[j:]
        return r

    def count(self, prefix, start, end, lower, upper):
        if start >= end:
            return 0

        mid = start + (end - start + 1 >> 1)
        count = sum([
            self.count(prefix, s, e, lower, upper)
            for s, e in ((start, mid - 1), (mid, end))
        ])

        l, r = mid, mid
        for i in xrange(start, mid):
            while l <= end and prefix[l] - prefix[i] < lower:
                l += 1
            while r <= end and prefix[r] - prefix[i] <= upper:
                r += 1
            count += r - l

        prefix[start:end + 1] = self.merge(
            prefix[start:mid], prefix[mid:end + 1])

        return count

    def countRangeSum(self, nums, lower, upper):
        n = len(nums)

        prefix = [0] * (n + 1)
        for i, v in enumerate(nums, 1):
            prefix[i] = prefix[i - 1] + v

        return self.count(prefix, 0, n, lower, upper)


s = Solution()
print s.countRangeSum([-2, 5, -1], -2, 2)
