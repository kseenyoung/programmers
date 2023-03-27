def solution(s):
    # 내 풀이
    i = 0 #position
    result = ''
    while i < len(s):
        if s[i].isdigit(): #digit
            result += s[i]
            i += 1
        elif s[i] == 'o': #one
            i += 3
            result += '1'
        elif s[i] == 't':
            if s[i+1] == 'h': #three
                i += 5
                result += '3'
            else: #two
                i += 3
                result += '2'
        elif s[i] == 'f':
            if s[i+1] == 'o': #four
                result += '4'
            else: #five
                result += '5'
            i += 4
        elif s[i] == 's':
            if s[i+1] == 'i': #six
                i += 3
                result += '6'
            else:
                i += 5 #seven
                result += '7'  # += 주의
        elif s[i] == 'e': #eight
            i += 5
            result += '8'
        elif s[i] == 'n': #nine
            i += 4
            result += '9'
        elif s[i] == 'z': #zero
            i += 4
            result += '0'
    return int(result)

    # 참조 풀이
    dic = {"one": '1', "two": '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

    for item, value in dic.items():
        s = s.replace(item, value)

    return(s)


print(solution("one4seveneight"))
