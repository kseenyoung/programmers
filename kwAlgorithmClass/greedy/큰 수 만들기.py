# stack Algo.
# 그리디 관점 : 앞 숫자가 최대한 크게
def solution(number, k):
    answer = []
    number = [int(i) for i in number]

    for i, n in enumerate(number):
        while answer and n > answer[-1] and k:
            answer.pop()
            k -= 1
        if k == 0:
            answer += number[i:]
            break
        answer.append(n)

    return ''.join(answer)

solution("1924",	2)