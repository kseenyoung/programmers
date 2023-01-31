def solution(tickets):
    contry = {}
    stack = ["ICN"]
    answer = []

    for f, t in tickets:
        if f not in contry:
            contry[f] = [t]
        else:
            contry[f].append(t)
    #다음으로 바꿀 수 있음
    '''
    for t in tickets:
    contry[t[0]] = contry.get(t[0], []) + t[1] #contry의 t[0] key의 값을 가져오 돼, 없으면 []으로 가져 옴.
    '''

    for c in contry:
        contry[c].sort(reverse=True)

    while stack: #stack에 값이 있을 때 동안(not 아님)
        f = stack[-1] #pop 연산 아님(끝에 도달 했을 때만 해당 값을 정답에 포함 시킬 것이기 때문)
        if f not in contry or len(contry[f]) == 0: #꺼낸 나라에서 다른 나라로 갈 수있는 곳이 없을 때 혹은 다 꺼냈을 때
            answer.append(stack.pop())
        else:
            c = contry[f].pop()
            stack.append(c)

    return answer[::-1] #반대로 출력

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
