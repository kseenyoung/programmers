def solution(number, k):
    answer = []
    for i, n in enumerate(number):
        if not answer:
            answer.append(n)
        else:
            while answer and answer[-1] < n and k:
                answer.pop()
                k -= 1
            if k == 0:
                answer += number[i:]  # 제거할 수 있는 수가 더이상 없을 때 현재 위치 부터 끝까지 이어 붙인다
                break
            answer.append(n)

    answer = answer[:-k] if k > 0 else answer

    return ''.join(answer)

solution("1924", 2)