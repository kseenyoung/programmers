from itertools import accumulate


def solution(bell):
    bell = [-1 if i == 1 else 1 for i in bell]
    new_bell = accumulate(bell)
    start = {}
    end = {}
    answer = 0

    for i, n in enumerate(new_bell):
        if n not in start:
            start[n] = i
        end[n] = i

    return max(end[x] - start[x] for x in end)


print(solution([1, 2, 1, 1, 1, 2, 2, 1]))