from collections import deque
def solution(numbers, target):
    que = deque()
    que.append((1, numbers[0]))
    que.append((1, -numbers[0]))
    result = 0

    while que:
        q = que.popleft()
        if q[0] == len(numbers):
            if q[1] == target:
                result += 1
        else:
            que.append((q[0]+1, q[1] + numbers[q[0]]))
            que.append((q[0]+1, q[1] - numbers[q[0]]))

    return result


print(solution([4,1,2,1], 4))


