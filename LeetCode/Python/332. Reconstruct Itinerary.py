# -*- coding: utf-8 -*-

'''
Given a list of airline tickets represented by pairs of departure and arrival
airports [from, to], reconstruct the itinerary in order. All of the tickets
belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
- If there are multiple valid itineraries, you should return the itinerary that
  has the smallest lexical order when read as a single string. For example, the
  itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
- All airports are represented by three capital letters (IATA code).
- You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].

Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But
it is larger in lexical order.
'''


import bisect
import collections


class Solution(object):
    def dfs(self, from_, graph, path):
        if not graph or self.r:
            self.r = self.r or path
            return

        if from_ not in graph:
            return

        for i, to in enumerate(graph[from_]):
            graph[from_].pop(i)
            if not graph[from_]:
                del graph[from_]

            self.dfs(to, graph, path + [to])
            bisect.insort_left(graph[from_], to)

    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for from_, to in tickets:
            bisect.insort_left(graph[from_], to)

        self.r = []
        self.dfs('JFK', graph, ['JFK'])
        return self.r
