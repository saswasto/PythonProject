import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        radj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            radj[v].append((u, w))

        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            if u == n - 1:
                return cost
            for v, w in adj[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))
            for v, w in radj[u]:
                new_cost = cost + 2 * w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1 if dist[n - 1] == INF else dist[n - 1]

        