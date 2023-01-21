def solution(numbers): #포인트 : Sort(내장함수) 정렬
    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x: (x*3)[:4], reverse=True)

    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)


print(solution([6, 10, 2]))
