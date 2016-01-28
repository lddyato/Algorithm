# -*- coding: utf-8 -*-

'''
Candy
=====

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following
requirements:

  - Each child must have at least one candy.
  - Children with a higher rating get more candies than their neighbors.
  - What is the minimum candies you must give?
'''


class Solution(object):
    '''算法思路：

    遍历 ratings，对于不同的 rating[i] rating[i - 1] 的关系做不同的操作

    结果：TLE
    '''
    def candy(self, ratings):
        length = len(ratings)

        i, candies = 1, [1] * length
        while i < length:
            if ratings[i] < ratings[i - 1] and candies[i - 1] == 1:
                candies[i - 1] += 1

                j = i - 2
                while (j >= 0 and ratings[j] > ratings[j + 1] and
                       candies[j] <= candies[j + 1]):

                    candies[j] += 1
                    j -= 1

            elif ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

            i += 1

        return sum(candies)


class Solution(object):
    '''算法思路：

    遍历 ratings，如果

    i: 当前遍历的 index
    pi: 递减数列的第一个数的 index
    pn: 递减数列的第一个数的 candies
    pre: index 为 i - 1 的 candies
    sm: candies 总和

    - rating[i] > rating[i - 1]
      pre += 1
      sm += pre + 1

    - ratings[i] < ratings[i - 1]
      如果 pre == 1，那么闭区间 [pi + 1, i - 1] 之间的 candies 全部都要 + 1，即
      sm += i - pi - 1，另外如果 pn <= candies[pi + 1] + 1 的话，sm += 1，最后
      加上当前 i 的 candies = 1, sm += 1

      最后 pre = 1

    - ratings[i]
      pre = 1

    结果：AC
    '''
    def candy(self, ratings):
        i, pi, pn, pre, sm, length = 1, 0, 1, 1, 1, len(ratings)

        while i < length:
            if ratings[i] > ratings[i - 1]:
                pre += 1

            elif ratings[i] < ratings[i - 1]:
                if pre == 1:
                    sm += i - pi - 1

                    if pn <= i - pi:
                        sm += 1
                        pn += 1

                pre = 1
            else:
                pre = 1

            sm += pre

            if (i + 1 < length and ratings[i] > ratings[i + 1] and
                    ratings[i] >= ratings[i - 1]):
                pi = i
                pn = pre

            i += 1

        return sm


class Solution(object):
    '''算法思路：

    正反遍历，得到结果

    结果：AC
    '''
    def candy(self, ratings):
        length = len(ratings)

        i, candies = 1, [1] * length
        while i < length:
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

            i += 1

        i = length - 2
        while i >= 0:
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

            i -= 1

        return sum(candies)


s = Solution()
print s.candy([1])
print s.candy([1, 2, 2])
print s.candy([2, 2, 1])
print s.candy([1, 3, 4, 3, 2, 1])
