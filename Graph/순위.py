INF = int(1e9)
def solution(n, results):
    graph = [[INF]*(n+1) for _ in range(n+1)]  # 인접 행렬
    result = 0

    for a, b in results:  # 직접 연관이 있는 관계 업데이트
        graph[a][b] = 1

    # 플로이드-워셜 알고리즘
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                # 행 열이 같다면 0, 다르다면 a -> b 와 a -> k -> b 중 짧은 거리 선택
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) if a != b else 0

    for i in range(1, n+1):
        flag = False  # 정점 i에 대해 i -> j 또는 j -> i로 갈 수 있는 방법이 있는지 판별
        for j in range(1, n+1):
            print(graph[i][j], end=" ")
            if i != j and graph[i][j] == INF and graph[j][i] == INF:
                flag = True  # 정점 i로부터 도달 할 수 없는 정점이 하나라도 있으면 순위를 알 수 없음
                # break
        if not flag:  # i 정점으로부터 모든 정점으로 도달 할 수 있다면
            result += 1
        print(i)

    return result
