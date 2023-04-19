from collections import deque


def solution(n, computers):
    que = deque()
    visited = [False] * n
    count = 0

    for vertex in range(n):
        if not visited[vertex]:  # 아직 방문하지 않은 시작 노드
            # BFS
            que.append(vertex)
            while que:  # queue에 값이 있는 동안
                q = que.popleft()
                visited[q] = True  # 방문 표시
                for i, v in enumerate(computers[q]):  # 만약 computer[q][i] = 1이라면 연결됨
                    if not visited[i] and v:  # 연결된 node가 방문하지 않았다면
                        que.append(i)
            count += 1  # 한 네트워크 완료
    return count


print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 1
print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 2
