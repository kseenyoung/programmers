def solution(N, number):
    dp = [set() for i in range(8)]  # 연산 횟수 별 만들 수 있는 수 저장(최대 연산, 8)
    for i in range(1, 9):  # {N}, {NN}, {NNN} ...
        dp[i - 1].add(int(str(N) * i))

    for i in range(8):  # 1~8번의 연산 횟수 별 수행
        for j in range(i):  # 8번째 연산이라면 1~7
            for op1 in dp[j]:
                for op2 in dp[i - j - 1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]:
            return i + 1
    return -1