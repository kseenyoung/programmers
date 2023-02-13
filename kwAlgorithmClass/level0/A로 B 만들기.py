def solution(before, after):
    # 시도1
    # before[::-1]
    # if before == after:
    #     return 1
    # else:
    #     return 0

    # 시도2
    # for i in range(len(before)):
    #     if before[len(before)-i-1] != after[i]:
    #         return 0
    # return 1

    # 정답 : 뒤집는 것이 아니라 순서를 바꿔서 만들 수 있는지 / sorted를 이용해서 해결도 가능
    count = {}
    for b in before:
        if b not in count:
            count[b] = 1
        else:
            count[b] += 1
    for a in after:
        if a not in count:
            count[a] = 1
        else:
            count[a] -= 1

    for c in count:
        if count[c] != 0:
            return 0
    return 1
