def solution(sizes):
    # 해결 못함
    # answer = set()
    # for w, h in sizes:
    #     answer.add((h, w))
    #     answer.add((w, h))
    #
    # print(answer)
    # minH = 1000
    # minW = 1000
    # answer = list(answer)
    #
    # for w, h in answer:
    #     if minH * minW > w * h:
    #         minH = h
    #         minW = w
    #
    # return minW * minH

    # 쌤 풀이
    a = [max(i) for i in sizes]  # 모든 값 중 최대 값
    b = [min(i) for i in sizes]  # 모든 값 중 최소 값
    return max(a) * max(b)  # 최댓값 중에 최댓값 * 최솟값 중에 최댓값
