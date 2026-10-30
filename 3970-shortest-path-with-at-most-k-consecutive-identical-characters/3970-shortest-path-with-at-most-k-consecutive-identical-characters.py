class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, labels[0], 1)]
        dist = {(0, labels[0], 1): 0}

        while pq:
            pq.sort(reverse=True)
            cost, node, last_char, count = pq.pop()

            state = (node, last_char, count)

            if cost != dist.get(state, float('inf')):
                continue

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:
                ch = labels[nei]

                if ch == last_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight
                new_state = (nei, ch, new_count)

                if new_cost < dist.get(new_state, float('inf')):
                    dist[new_state] = new_cost
                    pq.append((new_cost, nei, ch, new_count))

        return -1