def solution(n, lost, reserve):
    rlost = len(lost)
    for i in lost:
        if i - 1 in reserve:
            rlost -= 1
        elif i + 1 in reserve:
            rlost -= 1

    answer = n - rlost
    print(answer)

solution(5, [2, 4], [3])
