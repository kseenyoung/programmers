def solution(emergency):
    answer = [0] * len(emergency)  # 순서를 저장하기 위한 공간
    newEmer = []

    for i, n in enumerate(emergency):
        newEmer.append((i, n))
    newEmer.sort(key=lambda x: -x[1])

    for i, e in enumerate(newEmer, start=1):
        answer[e[0]] = i

    return answer