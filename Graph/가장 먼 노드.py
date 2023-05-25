from collections import deque
import heapq
INF = int(1e9)


def solution1(n, edge):
    que = deque()
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    que.append((1, 0))
    visited[1] = -1  # 1번 노드 방문 표시

    while que:  # BFS
        q = que.popleft()
        for v in graph[q[0]]:
            if not visited[v]:
                visited[v] = q[1] + 1
                que.append((v, q[1] + 1))

    return visited.count(max(visited))


def solution2(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)

    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    def dijkstra(start):
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + 1
                if distance[i] > cost:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))

    dijkstra(1)
    return distance.count(max(distance[1:]))


print(solution1(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution2(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))