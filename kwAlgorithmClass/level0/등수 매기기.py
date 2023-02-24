def solution(score):
    # 83% -> 100%
    blist = {}  # 등수를 담을 dic
    answer = [0] * len(score)
    alist = [[i, (n[0] + n[1]) // 2] for i, n in enumerate(score)]  # 나머지도 고려하여서 게산 해야한다. #[[1,2],[1,1]]
    alist.sort(key=lambda x: -x[1])
    for a in alist:
        if a[1] not in answer:
            blist[a[1]] = blist.get(a[1], []) + [a[0]]
        else:
            blist[a[1]].append(a[0])

    i = 1
    for b in blist:
        for a in blist[b]:
            answer[a] = i
        i += len(blist[b])

    return answer



print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))