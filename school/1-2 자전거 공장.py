#내 풀이(0%)
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


solution(5,	[2, 4],	[1, 3, 5])

#풀이1

