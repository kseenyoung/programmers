def solution(polynomial):
    alist = polynomial.split()
    print(alist)
    result = [0, 0]
    for i in range(0, len(alist), 2):
        if alist[i][-1] == 'x':
            if alist[i][:-1] == '':
                result[0] += 1
            else:
                result[0] += int(alist[i][:-1])
        else:
            result[1] += int(alist[i])
    answer = ''
    if result[0] > 0:
        if result[0] == 1:
            answer += 'x'
        else:
            answer += f"{result[0]}x"
        if result[1] > 0:
            answer += f" + {result[1]}"
    else:
        if result[1] > 0:
            answer += f"{result[1]}"

    return answer