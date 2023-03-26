def solution(left, right):
    answer = 0

    # solution 1(my)
    for n in range(left, right+1):
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        if count % 2 == 0:
            answer += n
        else:
            answer -= n

    # solution 2 : 제곱수 아닌 수의 약수는 각자의 짝이 있다 = 짝수
    for n in range(left, right+1):
        if int(n**0.5) == n**0.5:
            answer -= n  # 제곱수, 홀수
        else:
            answer += n  # 짝수


    return answer
