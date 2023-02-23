def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):  # len(my_str) 범위 주의
        print(i)
        answer.append(my_str[i:i + n])

    return answer