def solution(routes):
    #내 풀이
    # routes.sort(key=lambda x: (x[0],x[1]))
    # alist = [i for i in range(routes[0][0], routes[len(routes)-1][1])]
    # for r in routes:
    #     for i in range(r[0],r[1]+1):
    #         alist[i] += 1
    # return routes

    #쌤 풀이
    routes.sort(key=lambda x: x[1])
    camera = -30001
    answer = 0

    for r in routes:
        if camera < r[0]:
            camera = r[1]  # 진출 지점에 카메라를 놓음
            answer += 1

    return answer