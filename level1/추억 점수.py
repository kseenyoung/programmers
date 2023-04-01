def solution(name, yearning, photo):
    dic = {}
    result = []
    for i, n in enumerate(name):
        dic[n] = yearning[i]

    for pho in photo:
        temp = 0
        for p in pho:
            if p in dic:
                temp += dic[p]
        result.append(temp)

    return result

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))