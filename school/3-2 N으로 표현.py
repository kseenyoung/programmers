def solution(N, number):

    dp = [set() for _ in range(8)]
    for i, n in enumerate(dp, start=1):
        dp[i-1].add(int(str(N)*i))

    for i in range(1, len(dp)):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i - j - 1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 * op2)
                    dp[i].add(op1 - op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]:
            return i + 1
    else:
        return -1

print(solution(5, 12))
