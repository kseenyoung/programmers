def solution(s):
    alist = s.split(" ")
    result = ''
    for a in alist:
        for i, b in enumerate(a):
            if b == ' ':
                result += ' '
            elif i % 2 == 0:
                result += b.upper()
            else:
                result += b.lower()
        result += ' '

    return result[:-1]


# 1)앞뒤 공백  2)공백이 1개 이상  3)대문자 섞임
print(solution("    hEllo WoRLD !!   "))
