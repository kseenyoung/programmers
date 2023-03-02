from queue import deque


def solution(n, edge):
    vertex = [[] for _ in range(n + 1)]
    que = deque()
    que.append(1)
    visited = [0] * (n + 1)
    visited[1] = 1

    for s, e in edge:
        vertex[s].append(e)
        vertex[e].append(s)
    # print(vertex)
    while que:
        a = que.popleft()
        for i in vertex[a]:
            if not visited[i]:  # 아직 방문하지 않은 노드
                que.append(i)
                visited[i] = visited[a] + 1
    print(visited)
    answer = visited.count(max(visited))
    return answer