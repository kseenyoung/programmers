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
    a = [max(i) for i in sizes]  # 모든 쌍 중 최대 값만
    b = [min(i) for i in sizes]  # 모든 쌍 중 최소 값만
    # a, b에는 모든 쌍들이 각각 1번씩만 들어 가게 된다. 쌍은 작거나 크거나 둘 증 하나 이므로
    return max(a) * max(b)  # 최댓값 중에 최댓값 * 최솟값 중에 최댓값
