def solution(cost, order):
    torder = 0
    for i in range(len(order)):
        torder += order[i][1]

    print("torder %d" % torder)
    for n in order:
        if n[1] / 50 > n[0]:
            pass

    answer = 0
    print(answer)


solution([[0, 10], [50, 20]], [[3, 100], [4, 200]])
