def solution(my_string):
    answer = 0
    temp = ''
    numcheck = False

    for s in my_string:
        if s.isdigit():  # 숫자라면
            numcheck = True
            temp += s
        else:
            if numcheck:  # 숫자가 아닌데 이전에 숫자가 있었다면
                answer += int(temp)
                temp = ''
            numcheck = False

    return answer


solution("aAb1B2cC34oOp")