
def solution(n, computers):
    visited = set()
    answer = 0

    def dfs(computer):
        for i, c in enumerate(computers[computer]):
            if i not in visited and c:
                visited.add(i)
                dfs(i)

    for c in range(len(computers )):
        if c not in visited:
            visited.add(c)
            dfs(c)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
