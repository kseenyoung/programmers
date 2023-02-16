def solution(N, number):
    # 내 풀이(44%)
    # answer = [[] for _ in range(9)]  # 각 인덱스 크기 만큼 횟수를 사용해 표현할 수 있는 리스트
    #
    # for i in range(1, len(answer)):
    #     answer[i].append(int(str(N)*i))
    #
    # for i in range(2, len(answer)):
    #     for a in answer[i-1]:
    #         answer[i].append(a+N)
    #         answer[i].append(a-N)
    #         answer[i].append(a*N)
    #         if a != 0:
    #             answer[i].append(a//N)
    #     if number in answer[i]:
    #         return i
    # else:
    #     return -1

    # 풀이
    answer = [set() for _ in range(9)]

    for i in range(1, len(answer) - 1):  # 1~8
        answer[i].add(int(str(N) * i))

    for i in range(1, len(answer)):  # 2~8(x)->1~8(o) : testcase9 , len(answer)..!: testcase 5,8
        for j in range(1, i + 1):

            for op1 in answer[j]:
                for op2 in answer[i - j]:
                    answer[i].add(op1 + op2)
                    answer[i].add(op1 - op2)
                    answer[i].add(op1 * op2)
                    if op2 != 0:
                        answer[i].add(op1 // op2)
            if number in answer[i]:
                return i
    else:
        return -1


print(solution(2, 11))
