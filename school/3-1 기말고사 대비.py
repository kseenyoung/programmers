#내 풀이
def solution(t, k, study, pstudy):
    answer = 0
    diffStudy = []

    for _ in range(k):
        minPstudy = min(pstudy)
        minIndex = pstudy.index(minPstudy)
        # if t - minPstudy < 0:
        #     break
        t -= minPstudy
        del pstudy[minIndex]
        del study[minIndex]
        answer += 1

    study.sort()
    i = 0
    while t > 0:
        if t - study[i] < 0:
            return answer + i
        t -= study[i]
        i += 1

    return answer + i




print(solution(10, 2, [8, 13, 8, 9, 5], [1, 3, 4, 7, 4]))
