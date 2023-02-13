def solution(numbers):
    answer = 0
    # 시도1 #원소에 최대와 최소밖에 없는 경우...! ex. [-3, 3]
    # for i in range(len(numbers)):
    #     for j in range(i):
    #         if answer < numbers[i]*numbers[j]:
    #             answer = numbers[i]*numbers[j]
    # return answer

    # 정답
    numbers.sort()
    a1 = numbers[0]*numbers[1]
    a2 = numbers[-1]*numbers[-2]
    return a1 if a1 > a2 else a2


solution([1, 2, -3, 4, -5])