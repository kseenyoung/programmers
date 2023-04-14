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

# 풀이4(96.3% 22번 시간초과 -> 100% Count & filter 사용)
from collections import Counter
def solution(N, stages):
    # stage = {i: 0 for i in range(1, N + 2)}  # 0번 N번 스테이지 포함
    count = Counter(stages)  # for문 -> Counter()
    # for s in stages:
    #     for j in range(s, 0, -1):
    #         stage[j] += 1

    result = []
    for i in range(1, N + 1):
        clearCount = len(list(filter(lambda x:x >= i, stages)))  # 본인 보다 크거나 같은 수 카운트(해당 스테이지 도달한 유저 수)
        if clearCount != 0:  # stage[i] -> clearCount
            result.append((count[i] / clearCount, i))
        else:
            result.append((0, i))
    result.sort(key=lambda x: -x[0])
    return [i[1] for i in result]








