def solution(n, lost, reserve):
    answer = [1]*(n+2)
    for r in reserve:
        answer[r] += 1
    for l in lost:
        answer[l] -= 1

    for i in range(1, len(answer)):
        if answer[i] == 2 and answer[i-1] == 0:
            answer[i-1:i+1] = [1, 1]
        if answer[i] == 2 and answer[i+1] == 0:
            answer[i:i+2] = [1, 1]

    return n - answer.count(0)
