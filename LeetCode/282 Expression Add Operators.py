# -*- coding: utf-8 -*-

'''
Expression Add Operators
========================

Given a string that contains only digits 0-9 and a target value, return all
possibilities to add binary operators (not unary) +, -, or * between the
digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
'''


import operator


class Solution(object):
    '''算法思路：

    运用栈来辅助运算，中缀转后缀，然后运算

    结果：TLE

    通过 profile 分析程序，search 调用次数太多，因为有重复的，所以可以优化，另外
    append 和 pop 也占用了大量时间
    '''
    funcs = [operator.add, operator.sub, operator.mul]
    priority = [0, 0, 1]
    ops = ['+', '-', '*']

    def search(self, num, n, pointer, target, path, operators, operands, r):
        if pointer >= n:
            path.pop()
            operators.pop()

            while operators:
                f, b, a = self.funcs[operators.pop()], operands.pop(), operands.pop()
                operands.append(f(a, b))

            if operands[0] == target:
                r.add(''.join(path))
            return

        for j in xrange(pointer, n):
            if not (j == pointer or j > pointer and num[pointer] != '0'):
                break

            new = num[pointer:j + 1]

            for i in xrange(3):
                _ors, _ods = operators[:], operands + [int(new)]

                while _ors and self.priority[i] <= self.priority[_ors[-1]]:
                    f, b, a = self.funcs[_ors.pop()], _ods.pop(), _ods.pop()
                    _ods.append(f(a, b))
                _ors.append(i)

                self.search(
                    num, n, j + 1, target, path + [new, self.ops[i]], _ors, _ods, r)

    def addOperators(self, num, target):
        if not num:
            return []

        r = set()
        self.search(num, len(num), 0, target, [], [], [], r)
        return list(r)


class Solution(object):
    '''算法思路：

    这次不用栈，去掉了 append, pop 操作

    结果：TLE

    分析，还可以通过减少 search 调用次数来减少时间
    '''
    def search(self, num, n, pointer, target, expression, path, r):
        if pointer >= n:
            if sum(expression) == target:
                path.pop()
                r.add(''.join(path))
            return

        for i in xrange(pointer, n):
            if not (i == pointer or num[pointer] != '0'):
                break

            numberStr = num[pointer:i + 1]
            numberInt = int(numberStr)

            op = path and path[-1] or ''
            if op == '*':
                expression[-1] = expression[-1] * numberInt

            for o in ['+', '-', '*']:
                self.search(
                    num, n, i + 1, target,
                    expression + ([] if op == '*' else [int(op + numberStr)]),
                    path + [numberStr, o], r
                )

    def addOperators(self, num, target):
        r = set()
        self.search(num, len(num), 0, target, [], [], r)
        return list(r)


class Solution(object):
    '''算法思路：

    通过减少 search 的调用次数，是上述解法的 1/3 倍

    结果：AC
    '''
    def search(self, num, n, pointer, target, expression, path, r):
        if pointer >= n:
            if sum(expression) == target:
                r.append(''.join(path))
            return

        for i in xrange(pointer, n):
            if not (i == pointer or num[pointer] != '0'):
                break

            number = num[pointer:i + 1]

            for o in ['+', '-']:
                self.search(
                    num, n, i + 1, target, expression + [int(o + number)],
                    path + [o, number], r
                )

            old, expression[-1] = expression[-1], expression[-1] * int(number)
            self.search(
                num, n, i + 1, target, expression, path + ['*', number], r)
            expression[-1] = old

    def addOperators(self, num, target):
        n, r = len(num), []
        for i in xrange(1, n + 1):
            if i == 1 or num[0] != '0':
                self.search(num, n, i, target, [int(num[:i])], [num[:i]], r)
        return r


s = Solution()
print s.addOperators("2147483647", 2147483647)
