# 너비 우선 탐색(큐)
from collections import deque
def solution(numbers, target):
    que = deque()
    q = deque()
    answer = 0

    #내 풀이
    # for i, n in enumerate(numbers):
    #     if i == 0:
    #         que.append(n)
    #         que.append(-n)
    #         print(que)
    #     else:
    #         q = que.popleft()
    #         print(q)
    #         if q == target:
    #             answer += 1
    #         else:
    #             que.append(q + n)
    #             que.append(q - n)
    #
    # for q in que:
    #     if q == target:
    #         answer += 1
    #
    # return que.count(target)

    #풀이
    n = len(numbers)

    q.append([numbers[0], 0]) #0번째 숫자를
    q.qppend([-numbers[0], 0])

    while q:
        value, idx = q.popleft()
        idx += 1
        if idx < n:  #n회차 연산보다 작은지 확인
            q.append([value + numbers[idx], idx])
            q.append([value - numbers[idx], idx])
        else:
            if value == target:
                answer += 1

    return answer