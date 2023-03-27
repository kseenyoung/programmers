def solution(N, stages):
    # 풀이1(66%)
    # 각 stage 별 도달 유저 수
    stage = {}
    result = []
    for i in range(1, N + 1):
        stage[i] = stages.count(i) / len(list(filter(lambda x: x >= i, stages)))
    # print(stage)
    stage = sorted(stage.items(), key=lambda x: -x[1])
    for s in stage:
        result.append(s[0])

    return result

# 풀이2(96%)
def solution(N, stages):
        # 각 stage 별 도달 유저 수
        stage = {}
        result = []
        for i in range(1, N + 1):
            temp = len(list(filter(lambda x: x >= i, stages)))
            if temp != 0:  # 나누는 수가 0인 경우 처리
                stage[i] = stages.count(i) / temp
            else:
                stage[i] = 0

        stage = sorted(stage.items(), key=lambda x: -x[1])
        print(stage)
        for s in stage:
            result.append(s[0])

        return result

# 풀이3
def solution(N, stages):
    # 각 stage 별 도달 유저 수
    stage = {}
    result = []
    for i in range(1, N + 1):
        temp = len(list(filter(lambda x: x >= i, stages)))
        if temp != 0:  # 미처리 시(72%)
            stage[i] = stages.count(i) / temp
        else:
            stage[i] = 0.0  # 0일 때 0과 0.0 비교 문제 발생(testcase 9)

    stage = sorted(stage.items(), key=lambda x: -x[1])
    print(stage)
    for s in stage:
        result.append(s[0])

    return result









