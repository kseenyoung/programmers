from itertools import product
from collections import deque
def solution(numbers, target):
    # 방법1
    # l = [(x, -x) for x in numbers]
    # s = list(map(sum, product(*l)))
    # return s.count(target)

    #방법2
    answer = 0
    que = deque()
    que.append(numbers[0], 1)
    que.append(-numbers[0], 1)
    count = len(numbers)
    while que:
        q = que.popleft()
        if count == que[1]:
            if q[1] == target:
                answer += 1
        else:
            que.append((q[0] + numbers[q[1]], q[1] + 1))
            que.append((q[0] - numbers[q[1]], q[1] + 1))

    return answer



print(solution([1, 1, 1, 1, 1], 3))
