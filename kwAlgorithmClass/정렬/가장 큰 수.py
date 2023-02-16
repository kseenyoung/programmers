def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    numbers.sort(key=lambda x: str(x)*3, reverse=True)

    return ''.join([str(i) for i in numbers])


print(solution([6, 10, 2]))