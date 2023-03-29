# 풀이1 (my)
def solution(babbling):
    result = 0
    for b in babbling:  #단어 하나씩 확인
        i = 0 #position
        temp = 0 #이전 문자 확인
        ttemp = True
        while i < len(b):
            if b[i] == 'a':
                if b[i:i+3] == 'aya' and temp != 1:
                    temp = 1
                    i += 3
                else:
                    ttemp = False
                    break
            elif b[i] == 'y':
                if b[i:i+2] == 'ye' and temp != 2:
                    temp = 2
                    i += 2
                else:
                    ttemp = False
                    break
            elif b[i] == 'w':
                if b[i:i+3] == 'woo' and temp != 3:
                    temp = 3
                    i += 3
                else:
                    ttemp = False
                    break
            elif b[i] == 'm':
                if b[i:i+2] == 'ma' and temp != 4:
                    temp = 4
                    i += 2
                else:
                    ttemp = False
                    break
            else:
                ttemp = False
                break
        if ttemp:
            result += 1
    return result

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

# 풀이2 (참고)
def solution(babbling):
    result = 0
    dic = ['aya', 'ma', 'ye', 'woo']
    for b in babbling:
        for d in dic:
            if d*2 not in b:
                b = b.replace(d, ' ')
        if b.rstrip() == '':
            result += 1
    return result