def solution(n):
    answer = 0

    for _ in range(n):
        answer += 1
        while '3' in str(answer) or answer % 3 == 0:
            answer += 1
        print(answer)

    return answer