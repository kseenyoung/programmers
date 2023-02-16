from collections import deque

def solution(prices):
    # 내 풀이(맞음)
    # answer = [0]*len(prices)
    # que = deque(prices)
    #
    # for i, p in enumerate(prices):
    #     q = que.popleft()
    #
    #     for j, a in enumerate(que, start=1):
    #         if a < q or j == len(que):
    #             answer[i] = j
    #             break
    #
    # return answer

    #  쌤 풀이
    box = []
    prices = deque(prices)

    while prices:
        a = prices.popleft()
        sec = 0
        for i in prices:
            if i >= a:
                sec += 1
            else:
                sec += 1
                break
        box.append(sec)

    return box

print(solution([1, 2, 3, 2, 3]	))
