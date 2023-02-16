def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = []

    for r in routes:
        if not answer:
            answer.append(r[1])
        else:
            for a in answer: # 이미 설치한 cctv에 루트가 곂치는 경우
                if r[0] <= a <= r[1]:
                    break
            else:  # 이미 설치한 cctv 어디에도 걸리지 않는 경우
                    answer.append(r[1])

    return answer

    # 쌤 풀이
    routes.sort(key=lambda x: x[1])
    camera = -30001
    answer = 0

    for r in routes:
        if camera < r[0]:
            camera = r[1]  # 진출 지점에 카메라를 놓음
            answer += 1

    return answer
