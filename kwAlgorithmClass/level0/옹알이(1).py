def solution(babbling):
    result = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for bab in babbling:
        tempbab = bab
        i=0
        while tempbab != '':
            if tempbab[:3] == 'aya': #aya
                tempbab = tempbab[3:]
            elif tempbab[:2] == 'ye': #ye
                tempbab = tempbab[2:]
            elif tempbab[:3] == 'woo': #woo
                tempbab = tempbab[3:]
            elif tempbab[:2] == 'ma': #ma
                tempbab = tempbab[2:]
            else:
                break
        if tempbab == '':
            answer += 1
    return answer