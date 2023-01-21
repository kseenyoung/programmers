def solution(storey):
    if storey <= 1:
        return storey
    d, m = divmod(storey, 10)
    return min(solution(d) + m, solution(d+1) + (10-m))