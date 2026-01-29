class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 1 << 25
        graph = [[] for _ in range(26)]
        for a, b, c in zip(original, changed, cost):
            x = ord(a) - ord('a')
            y = ord(b) - ord('a')
            graph[x].append((y, c))

        def dijkstra(start):
            dist = [INF] * 26
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))
            return dist
        compute = [dijkstra(i) for i in range(26)]
        total = 0
        for s, t in zip(source, target):
            si = ord(s) - ord('a')
            ti = ord(t) - ord('a')
            d = compute[si][ti]
            if d >= INF:
                return -1
            total += d
        return total
