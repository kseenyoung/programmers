# 풀이(31.6%)
def solution(X, Y):
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
    result = [0] * 9
    for i in tempX:
        if i in tempY:
            result[int(i)] = min(tempX[i], tempY[i])
    if not sum(result):
        return "-1"
    else:
        answer = ''
        for i, a in enumerate(reversed(result)):
            if a != 0:
                answer += str(len(result)-1-i)*a
        return answer if int(answer) != 0 else '0'


print(solution("5525", "1255"))
