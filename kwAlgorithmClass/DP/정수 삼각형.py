def solution(triangle):
    # for i in range(1, len(triangle)):
    #
    #     for k, t in enumerate(triangle[i]):
    #         if k == 0:
    #             triangle[i][k] += triangle[i - 1][k]
    #         elif k == len(triangle[i]) - 1:
    #             triangle[i][k] += triangle[i - 1][-1]
    #         else:
    #             triangle[i][k] += max(triangle[i - 1][k - 1], triangle[i - 1][k])
    # return max(triangle[len(triangle) - 1])

    #쌤 풀이
    dp = [[0]*len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])




solution()