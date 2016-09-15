# -*- coding: utf-8 -*-

'''
Permutation Sequence
====================

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''


class Solution(object):
    '''算法思路：

    暴力枚举，观察结果可以看到：序列是对称的，可以根据这一点进行优化（这里没有优化）

    结果: Time Limit Exceeded
    '''
    def getPermutation(self, n, k):
        def gen_permutation(sets):
            if len(sets) == 1:
                return map(str, sets)

            return sum([
                [str(v) + p for p in gen_permutation(sets[:i] + sets[i+1:])]
                for i, v in enumerate(sets)
            ], [])

        return gen_permutation(range(1, n + 1))[k - 1]


class Solution(object):
    '''算法思路：

    因为生成的字典序列是有序的，所以序列是有规律可循的。

    按照下标生成阶乘序列然后反转，得到 [(n-1)!, (n-2)!, (n-3)!, ... , 1!, 0!]

    (k - 1 - 已经处理的所有的 商x阶乘 的和) 从前往后除以每一个阶乘，得到一个 商 的序列

    商的序列中每个值是有意义的，它代表在第 k-1 个字典中与商的索引对应的字符在当前
    字符集中的索引

    举个例子：当 n = 4，k = 11

    序列为：
    ['1234', '1243', '1324', '1342', '1423', '1432', '2134', '2143', '2314',
     '2341', '2413', '2431', '3124', '3142', '3214', '3241', '3412', '3421',
     '4123', '4132', '4213', '4231', '4312', '4321']

    阶乘序列为：factorials = [6, 2, 1, 1]
    商的集合为：divs = [1, 2, 0, 0]
    原始字符集合为：sets = ['1', '2', '3', '4']

    从上面可以查到第k-1个序列为 '2413'，也即我们的结果，下面分析一下 '2413'是怎么来的，
    假设我们要求的结果为 result，初始值为空，即 result=''

    首先从字符集合 sets 中取出索引为 1 的字符 '2'，得到result += '2'即 result = '2'
    然后把 '2' 从字符集合中删除，得到 sets = ['1', '3', '4']
    接着从 sets 中取出索引为 2 的字符 '4'，得到 result += '4' 即 result = '24'
    把 '4' 从字符集合中删除，得到 sets = ['1', '3']
    接着从 sets 中取出索引为 0 的字符 '1'，得到 result += '1' 即 result = '241'
    把 '1' 从字符集合中删除，得到 sets = ['3']
    最后从 sets 中取出索引为 0 的字符 '3'，得到 result += '3' 即 result = '2413'

    就得到了我们的结果 '2413'，和上面查到的一模一样
    '''
    def getPermutation(self, n, k):
        factorials, i = [1], 1
        while i < n:
            factorials.insert(0, factorials[0] * i)
            i += 1

        divs, i, s = [], 0, 0
        while i < n:
            div = (k - 1 - s) / factorials[i]
            s += factorials[i] * div
            divs.append(div)

            i += 1

        i, result, sets = 0, [], range(1, n + 1)
        while i < len(divs):
            result.append(sets[divs[i]])
            del sets[divs[i]]
            i += 1

        return ''.join(map(str, result))


import math


class Solution(object):
    """算法思路：

    同上，只不过是另外一种写法
    """
    def getPermutation(self, n, k):
        r, token = [], [False] * n

        for i in xrange(n - 1, -1, -1):
            div = max(k - 1, 0) / math.factorial(i)
            k -= div * math.factorial(i)

            cnt = 0
            for j, t in enumerate(token, 1):
                if t:
                    continue

                if cnt == div:
                    r.append(j)
                    token[j - 1] = True
                    break

                cnt += 1

        return ''.join(map(str, r))


s = Solution()
s.getPermutation(4, 11)
