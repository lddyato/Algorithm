# -*- coding: utf-8 -*-

'''
Alien Dictionary
================

There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of words from the
dictionary, where words are sorted lexicographically by the rules of this new
language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
 "ett",
  "rftt"
]

The correct order is: "wertf".

Note:

- You may assume all letters are in lowercase.
- If the order is invalid, return an empty string.
- There may be multiple valid order of letters, return any one of them is fine.
'''


import collections


class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.children = []


class Graph(object):
    def __init__(self):
        self.graph = collections.defaultdict(set)
        self.v = collections.defaultdict(int)

    def addEdage(self, start, to=None):
        if not to and start not in self.graph:
            self.graph[start] = set()

        elif to and to not in self.graph[start]:
            self.graph[start].add(to)
            self.v[to] += 1

        if start not in self.v:
            self.v[start] = 0

    def topoSort(self):
        queue, r = collections.deque(
            char for char, count in self.v.items() if not count), []

        while queue:
            root = queue.popleft()
            r.append(root)
            for node in self.graph[root]:
                self.v[node] -= 1
                if not self.v[node]:
                    queue.append(node)
            del self.graph[root]

        return ''.join(r) if not self.graph else ''


class Solution(object):
    def alienOrder(self, words):
        trie, graph = TrieNode(), Graph()
        for word in words:
            root = trie

            for char in word:
                current = None

                for child in root.children:
                    if child.char == char:
                        current = child
                    else:
                        graph.addEdage(child.char, char)

                if current is None:
                    root.children.append(TrieNode(char))
                    root = root.children[-1]
                    graph.addEdage(char)
                else:
                    root = current

        return graph.topoSort()


s = Solution()
print s.alienOrder(["za","zb","ca","cb"])
