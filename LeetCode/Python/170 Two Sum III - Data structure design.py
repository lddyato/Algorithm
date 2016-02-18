# -*- coding: utf-8 -*-

'''
Two Sum III - Data structure design
===================================

Design and implement a TwoSum class. It should support the following
operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the
value.

For example,
    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false
'''


class TwoSum(object):
    '''算法思路：

    利用二分法维护一个有序数组，利用两边夹逼的办法去查询

    add:  O(logn)
    find: O(n)

    结果：Time Limit Exceeded
    '''
    def __init__(self):
        self.nums = []

    def add(self, number):
        nums = self.nums

        low, high, index = 0, len(nums) - 1, len(nums)
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] < number:
                low = mid + 1
            else:
                if (mid == 0) or (mid > 0 and nums[mid - 1] < number):
                    index = mid
                    break
                high = mid - 1

        nums.insert(index, number)

    def find(self, value):
        nums = self.nums
        low, high = 0, len(nums) - 1

        while low < high:
            s = nums[low] + nums[high]
            if s < value:
                low += 1
            elif s > value:
                high -= 1
            else:
                return True

        return False


class TwoSum(object):
    '''算法思路：

    维护一个每两个数的 sum hash

    add: O(n)
    find: O(1)

    结果：Time Limit Exceeded
    '''

    def __init__(self):
        self.nums = []
        self.sums = {}

    def add(self, number):
        for i in self.nums:
            self.sums[i + number] = 1

        self.nums.append(number)

    def find(self, value):
        return value in self.sums


class TwoSum(object):
    '''算法思路：

    维护一个数组，每次 add 到数组最后面，find 的时候利用 hash 保存已经遍历的 num

    add: O(1)
    find: O(n)

    结果：Time Limit Exceeded
    '''
    def __init__(self):
        self.nums = []

    def add(self, number):
        self.nums.append(number)

    def find(self, value):
        maps = {}
        for n in self.nums:
            left = value - n
            if left in maps:
                return True
            maps[n] = 1

        return False


import collections


class TwoSum(object):
    '''
    维护一个 {value: count} 的 hash, 直接遍历查询

    add: O(1)
    find: O(n)

    分析：这种算法和上面这个算法有点类似，区别在于上面的算法查询的时候每次都需要
    生成一个 hash，而且多了一个要维护的 nums 数组

    结果：Accepted

    结论: 看到一个不过的测试用例，多半是 add 操作，find 操作相对来说比较少，因此这种
    写法会 AC
    '''
    def __init__(self):
        self.record = collections.defaultdict(int)

    def add(self, number):
        self.record[number] += 1

    def find(self, value):
        r = self.record
        for num in r:
            left = value - num
            if left != num and left in r or left == num and r[num] > 1:
                return True
        return False


s = TwoSum()
s.add(2)
s.add(1)
s.add(1)
s.add(5)
s.add(4)
s.add(78)

print s.find(2)
