# -*- coding: utf-8 -*-

'''
Create Maximum Number
=====================

Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two. The
relative order of the digits from the same array must be preserved. Return an
array of the k digits. You should try to optimize your time and space
complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
'''


class Solution(object):
    '''算法思路：

    每次从中挑选出来一个直到挑选出来 k 个

    结果：TLE
    '''
    def compare(self, nums1, nums2):
        for i in xrange(len(nums1)):
            if nums1[i] > nums2[i]:
                return nums1

            if nums1[i] < nums2[i]:
                return nums2
        return nums1

    def merge(self, nums1, nums2):
        i, j, m, n, r = 0, 0, len(nums1), len(nums2), []

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                r.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                r.append(nums2[j])
                j += 1
            else:
                r.append(nums1[i])

                left1 = self.merge(nums1[i:], nums2[j+1:])
                left2 = self.merge(nums1[i+1:], nums2[j:])

                return r + self.compare(left1, left2)

        r += nums1[i:] or nums2[j:]
        return r

    def choose(self, nums, k):
        if k >= len(nums):
            return nums

        if k <= 0:
            return []

        if k == 1:
            return [max(nums)]

        nums1 = nums[:1] + self.choose(nums[1:], k - 1)
        if len(nums1[1:]) >= k:
            nums2 = self.choose(nums[1:], k)
            return self.compare(nums1, nums2)
        return nums1

    def search(self, nums1, nums2, k):
        if k >= len(nums1) + len(nums2):
            return self.merge(nums1, nums2)

        if k <= 0:
            return []

        if k == 1:
            return [max(nums1 + nums2)]

        if not (nums1 and nums2):
            nums = nums1 or nums2
            return self.choose(nums, k)

        left1 = nums1[:1] + self.search(nums1[1:], nums2, k - 1)
        left2 = nums2[:1] + self.search(nums1, nums2[1:], k - 1)

        left1 = self.compare(left1, left2)

        if len(nums1) + len(nums2) - 1 >= k:
            left2 = self.search(nums1[1:], nums2, k)
            left3 = self.search(nums1, nums2[1:], k)
            return self.compare(left1, self.compare(left2, left3))

        return left1

    def maxNumber(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if k >= m + n:
            return self.merge(nums1, nums2)

        return self.search(nums1, nums2, k)


class Solution(object):
    '''算法思路：

    同上，只不过把结果缓存起来

    结果：TLE
    '''
    def cacheChoose(f):
        def method(obj, nums, start, end, k, which):
            key = '{}:{}:{}:{}'.format(which, start, end, k)
            if key not in obj.r1:
                obj.r1[key] = f(obj, nums, start, end, k, which)
            return obj.r1[key]
        return method

    def cacheSearch(f):
        def method(obj, nums1, start1, end1, nums2, start2, end2, k):
            key = '{}:{}:{}:{}:{}'.format(start1, end1, start2, end2, k)
            if key not in obj.r2:
                obj.r2[key] = f(
                    obj, nums1, start1, end1, nums2, start2, end2, k)
            return obj.r2[key]
        return method

    def genNumber(self, nums):
        s = 0
        for i, num in enumerate(nums):
            s = s * 10 + num
        return s

    def genList(self, num):
        return map(int, str(num))

    def merge(self, nums1, start1, end1, nums2, start2, end2):
        i, j, s = start1, start2, 0

        while start1 <= i <= end1 and start2 <= j <= end2:
            if nums1[i] > nums2[j]:
                s = s * 10 + nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                s = s * 10 + nums2[j]
                j += 1
            else:
                s = s * 10 + nums1[i]

                left1 = self.merge(nums1, i, end1, nums2, j + 1, end2)
                left2 = self.merge(nums1, i + 1, end1, nums2, j, end2)

                return s * 10 ** (end1 - i + 1 + end2 - j) + max(left1, left2)

        return s * 10 ** (end1 + 1 - i + end2 - j + 1) + self.genNumber(
            nums1[i:end1 + 1] or nums2[j:end2 + 1])

    @cacheChoose
    def choose(self, nums, start, end, k, which):
        stack = []

        for i in xrange(start, end + 1):
            while (end - i + 1 + len(stack) > k and stack and
                    nums[i] >= stack[-1]):
                stack.pop()
            stack.append(nums[i])

        return self.genNumber(stack)

    @cacheSearch
    def search(self, nums1, start1, end1, nums2, start2, end2, k):
        if k >= end1 - start1 + 1 + end2 - start2 + 1:
            return self.merge(nums1, start1, end1, nums2, start2, end2)

        if k == 1:
            return max(nums1[start1:end1 + 1] + nums2[start2:end2 + 1])

        if not (start1 <= end1 and start2 <= end2):
            if start1 > end1:
                return self.choose(nums2, start2, end2, k, 'j')
            return self.choose(nums1, start1, end1, k, 'i')

        if nums1[start1] > nums2[start2]:
            left1 = nums1[start1] * 10 ** (k - 1) + self.search(
                nums1, start1 + 1, end1, nums2, start2, end2, k - 1)
        elif nums1[start1] < nums2[start2]:
            left1 = nums2[start2] * 10 ** (k - 1) + self.search(
                nums1, start1, end1, nums2, start2 + 1, end2, k - 1)
        else:
            left1 = nums1[start1] * 10 ** (k - 1) + self.search(
                nums1, start1 + 1, end1, nums2, start2, end2, k - 1)
            left2 = nums2[start2] * 10 ** (k - 1) + self.search(
                nums1, start1, end1, nums2, start2 + 1, end2, k - 1)
            left1 = max(left1, left2)

        if end1 - start1 + 1 + end2 - start2 >= k:
            left2 = self.search(
                nums1, start1 + 1, end1, nums2, start2, end2, k)
            left3 = self.search(
                nums1, start1, end1, nums2, start2 + 1, end2, k)

            return max(left1, left2, left3)

        return left1

    def maxNumber(self, nums1, nums2, k):
        if k <= 0 or not (nums1 and nums2):
            return []

        m, n = len(nums1), len(nums2)
        if k >= m + n:
            return self.genList(
                self.merge(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1))

        self.r1 = {}
        self.r2 = {}

        return self.genList(
            self.search(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, k))



class Solution(object):
    '''算法思路:

    分治法，分别从两个数组中挑选 (i, k-i) 个，然后选出最大的

    结果：AC
    '''
    def choose(self, nums, k):
        stack, n = [], len(nums)
        for i in range(n):
            while stack and nums[i] > stack[-1] and len(stack) + n - i - 1 >= k:
                stack.pop()

            if len(stack) < k:
                stack.append(nums[i])

        return stack

    def merge(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]

    def maxNumber(self, nums1, nums2, k):
        return max([
            self.merge(self.choose(nums1, i), self.choose(nums2, k - i))
            for i in range(k + 1)
            if 0 <= i <= len(nums1) and 0 <= k - i <= len(nums2)
        ])


s = Solution()
print s.maxNumber([5,5,1], [4,0,1], 3)
