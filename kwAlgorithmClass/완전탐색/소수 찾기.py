def solution(n):
    # answer = 0
    # for i in range(2, n + 1):
    #     for j in range(2, i):  # i까지 주의
    #         if i % j == 0:  # 소수가 아님
    #             break
    #     else:
    #         print(i)
    #         answer += 1
    #
    # return answer

    #쌤 풀이 - 에라토스테네스 체
    box = [True]*(n+1)
    box[0:2] = [False, False]
    for i in range(2, n+1):
        for j in range(i*2, n+1, i):  # point!
            box[j] = False
    print(box)


solution(5)
