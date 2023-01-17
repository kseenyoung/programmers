def solution(numbers):
    string = {}
    answer = ''
    for i in range(9, 0, -1):
        string[str(i)] = []

    for i in numbers:
        chrN = str(i)
        F = chrN[0]
        string[F] += [chrN]

    for i in string:
        if string[i]:
            string[i].sort(reverse=True)
            for a in string[i]:
                answer += a

    return answer


print(solution([6, 10, 2]))


# 풀이
def solution1(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(key=lambda x: (x * 4)[:4])

    if numbers[0] == '0':
        return numbers[0]
    return ''.join(numbers)