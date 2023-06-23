def solution(n):
    answer = 0
    dp = [1] * 10001

    for i in range(1, n + 1):
        temp = i
        for j in range(i + 1, n + 1):
            if temp + j > 10000:
                break
            temp += j
            dp[temp] += 1

    return dp[n]