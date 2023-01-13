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


def solution1(n, lost, reserve):
    #reserve가 학생 수보다 작을 때 : O(klogk)
    s = set(lost) & set(reserve) #&는 교집합
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x+1)
    return n - len(l)