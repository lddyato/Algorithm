# -*- coding: utf-8 -*-

'''
Integer to English Words
========================

Convert a non-negative integer to its english words representation. Given input
is guaranteed to be less than 2^31 - 1.

For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''


class Solution(object):
    '''算法思路：

    将数字从后往前每 3 位划分为一组，先处理每一组，然后再为每一组加上单位
    '''
    def dealOne(self, num):
        maps = {
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
        }
        return [maps[num]] if num in maps else []

    def dealTwo(self, num):
        maps1 = {
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen',
            '20': 'Twenty',
            '30': 'Thirty',
            '40': 'Forty',
            '50': 'Fifty',
            '60': 'Sixty',
            '70': 'Seventy',
            '80': 'Eighty',
            '90': 'Ninety'
        }

        maps2 = {
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '6': 'Sixty',
            '7': 'Seventy',
            '8': 'Eighty',
            '9': 'Ninety',
        }

        if num in maps1:
            return [maps1[num]]

        if num[0] != '0':
            return [maps2[num[0]]] + self.dealOne(num[1])

        return self.dealOne(num[1])

    def dealThree(self, num):
        r = []
        if num[0] != '0':
            r += ['{} Hundred'.format(self.dealOne(num[0])[0])]

        r += self.dealTwo(num[1:])
        return r

    def deal(self, num):
        return {
            1: self.dealOne,
            2: self.dealTwo,
            3: self.dealThree
        }[len(num)](num)

    def numberToWords(self, num):
        if not num:
            return 'Zero'

        num = str(num)
        n, maps = len(num), {1: ['Thousand'], 2: ['Million'], 3: ['Billion']}

        r, count = [], 0
        while n > 0:
            part = self.deal(num[max(n - 3, 0):n])
            if part:
                r = part + maps.get(count, []) + r
            n -= 3
            count += 1

        return ' '.join(r)


s = Solution()
print s.numberToWords('2147483647')
