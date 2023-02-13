def solution(box, n):
    # 도전1
    # answer = (box[0]*box[1]*box[2])//n**3
    # return answer

    # 도전2
    answer = (box[0] // n) * (box[1] // n) * (box[2]) // n
    return answer

    # 정답
    answer = (box[0]//n)*(box[1]//n)*(box[2]//n)  # 괄호 주의
    return answer
