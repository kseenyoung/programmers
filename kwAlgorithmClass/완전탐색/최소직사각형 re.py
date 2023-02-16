def solution(sizes):
    a = [max(aCouple) for aCouple in sizes]
    b = [min(aCouple) for aCouple in sizes]
    return max(a) * max(b)