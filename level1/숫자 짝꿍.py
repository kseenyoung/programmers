# 풀이1(31.6%->73.7%)
def solution(X, Y):
    # 각 문자열에서 어떤 문자가 얼마나 발생했는지 카운트
    tempX = {}
    tempY = {}
    for i in X:
        if i in tempX:
            tempX[i] += 1
        else:
            tempX[i] = 1
    for i in Y:
        if i in tempY:
            tempY[i] += 1
        else:
            tempY[i] = 1

    # 문자는 0-9 중 하나
    result = [0] * 10  # 9->10 (런타임 에러)
    # 각 문자열에서 일치하는 문자의 개수 구하기
    for i in tempX:
        if i in tempY:
            result[int(i)] = min(tempX[i], tempY[i])
    if not sum(result):  # 일치 하는 문자가 없을 때
        return "-1"
    else:
        # 일치 하는 문자 개수 만큼 큰 수부터 이어 붙이기
        answer = ''
        for i, a in enumerate(reversed(result)):
            if a != 0:
                answer += str(len(result) - 1 - i) * a
        return answer if int(answer) != 0 else '0'  # 0이 여러개(ex 000) 결과는 0




# 풀이2(참고)
def solution1(X, Y):
    result = ''.join([str(i)*min(X.count(str(i)), Y.count(str(i))) for i in range(9, -1, -1)])

    if result == '':
        return '-1'
    elif len(result) == result.count('0'):
        return '0'
    else:
        return ''.join(result)



print(solution1("100"	,"2345"))
print(solution1("100"	,"203045"))
print(solution1("100"	,"123450"))
print(solution1("12321"	,"42531"))
print(solution1("5525",	"1255"))

