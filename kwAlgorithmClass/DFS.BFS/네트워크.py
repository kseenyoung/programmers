from collections import deque

def solution(n, computers):
    # que = deque()  # bfs
    # answer = 0
    # visited = set()  # 방문한 노드 집합
    #
    # for computer, net in enumerate(computers):  # computer(노드)마다 방문
    #     if computer + 1 not in visited:  # 방문하지 않은 노드라면
    #         visited.add(computer + 1)  # 방문 표시
    #         que.append(computer + 1)
    #
    #         while que:
    #             q = que.pop()
    #             if q in computers and q not in visited:
    #                 for c in computers[q]:
    #                     if c not in visited:
    #                         que.append(i + 1)
    #                         visited.add(i + 1)
    #         answer += 1
    #
    # return answer

    #풀이

    def bfs(i):  # 컴퓨터 번호 입력
        q = deque()
        q.append(i)  # [0]
        while q:
            i = q.popleft()  # []
            visit[i] = 1
            for a in range(n):
                if computers[i][a] and visit[a] == 0:  #i컴퓨터 a번째 컴퓨터가 1이고, 아직 가본적 없다면
                    q.append(a)

    visit = [0]*n
    count = 0
    for i in range(n):
        if visit[i] == 0:
            bfs(i)  # 1이랑 연결되어 있는지, 2랑 연결되어 있는지 ......
            count += 1

    return count