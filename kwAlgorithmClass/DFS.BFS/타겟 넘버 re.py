from collections import deque
def solution(numbers, target):
    que = deque() # BFS
    idx = len(numbers)

    que.append((numbers[0], 1))
    que.append((-numbers[0], 1))

    answer = 0
    while que:
        q = que.popleft()
        if q[1] < idx:
            que.append((q[0]+numbers[q[1]], q[1] + 1))
            que.append((q[0]-numbers[q[1]], q[1] + 1))
        else:
            if q[0] == target:
                answer += 1

    return answer


print(solution([4,1,2,1], 4))