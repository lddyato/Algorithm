# -*- coding: utf-8 -*-

'''
Bulls and Cows
==============

You are playing the following Bulls and Cows game with your friend: You write
down a number and ask your friend to guess what the number is. Each time your
friend makes a guess, you provide a hint that indicates how many digits in said
guess match your secret number exactly in both digit and position (called
"bulls") and how many digits match the secret number but locate in the wrong
position (called "cows"). Your friend will use successive guesses and hints to
eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"

Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)

Write a function to return a hint according to the secret number and friend's
guess, use A to indicate the bulls and B to indicate the cows. In the above
example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate
digits, for example:

    Secret number:  "1123"
    Friend's guess: "0111"

In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow,
and your function should return "1A1B".

You may assume that the secret number and your friend's guess only contain
digits, and their lengths are always equal.
'''


import collections


class Solution(object):
    '''算法思路：

    可以把这道题看成生产者消费者问题，secret 是生产者，guess 是消费者
    '''
    def getHint(self, secret, guess):
        A, B, record = 0, 0, collections.defaultdict(int)
        for i, s in enumerate(secret):
            g = guess[i]
            if s == g:
                A += 1
            else:
                B += (record[s] < 0) + (record[g] > 0)
                record[s] += 1
                record[g] -= 1

        return '{}A{}B'.format(A, B)


class Solution(object):
    '''算法思路：

    算两边，第一次只算 A， 第二次只算 B
    '''
    def getHint(self, secret, guess):
        bulls, caws, record, r = 0, 0, collections.Counter(secret), []
        for i, num in enumerate(guess):
            if num == secret[i]:
                bulls += 1
                record[num] -= 1
            else:
                r.append(i)

        for i in r:
            if record[guess[i]]:
                caws += 1
                record[guess[i]] -= 1

        return '{}A{}B'.format(bulls, caws)


s = Solution()
print s.getHint('', '')
