from collections import deque
def solution(n, vertex):
    que = deque() # DFS
    visited = [-1]*(n+1)
    que.append(1)
    visited[1] = 1
    point = {}
    for v in range(1, n+1):
        point[v] = []

    for s, e in vertex:  # 간선 연결
        point[s].append(e)
        point[e].append(s)

    while que:  # 값이 있는 동안
        q = que.popleft()
        for v in point[q]:
            if visited[v] == -1:
                que.append(v)
                visited[v] = visited[q] + 1

    return visited.count(max(visited))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))