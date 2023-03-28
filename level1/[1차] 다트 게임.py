def solution(dartResult):
    result = []
    start = 0
    digit = 0
    for d in dartResult:
        if d.isdigit():  #점수
            if d == '0'and digit == 1:
                    digit = int(10)
            else:
                if start:
                    result.append(digit)
                digit = int(d)
            start = 1
        elif d.isupper(): #보너스
            if d == 'D':
                digit **= 2
            elif d == 'T':
                digit **= 3
        else:
            if d == '*':
                digit *= 2 #스타상
                if result:
                    result[-1] *= 2 #앞 스타상 적용
            if d == '#':
                digit *= -1

    if digit:
        result.append(digit)

    return sum(result)

print(solution("1S2D*3T"))

