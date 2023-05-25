INF = int(1e9)
def solution(n, results):
    graph = [[INF]*(n+1) for _ in range(n+1)]
    result = 0

    for a, b in results:
        graph[a][b] = 1

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) if a != b else 0

    for i in range(1, n+1):
        flag = False
        for j in range(1, n+1):
            if graph[i][j] == INF and graph[j][i] == INF:
                flag = True
                break
        if not flag:
            result += 1

    return result
