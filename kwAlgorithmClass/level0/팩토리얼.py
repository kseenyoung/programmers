def solution(n):
    #시도1
    if n == 1:  # testcase1
        return 1

    for i in range(2, n+1):  #n -> n+1 : testcase2,3
        answer = 1
        for j in range(2, i + 1):
            answer *= j

        if answer >= 3628800:
            return 10
        elif answer > n:
            return i - 1
        elif answer == n:
            return i