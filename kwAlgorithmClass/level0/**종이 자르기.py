# 참고
def solution(M, N):
    return M*N - 1

# 풀고 싶었던 방법(참고) but dp까지 확장 풀이 하고 싶었다..!
def solution(M, N):

    def dfs(m, n):
        if m == 1 and n == 1:
            return 0
        else:
            m, n = min(m, n), max(m, n)
            return 1 + dfs(m, n//2) + dfs(m, n-n//2)

