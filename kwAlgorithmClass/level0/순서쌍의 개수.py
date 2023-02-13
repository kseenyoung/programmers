def solution(n):
    answer = 0
    result = set()
    for i in range(n):
        if n % i == 0:
            result.add((i, n // i))

    return len(result)