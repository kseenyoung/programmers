def solution(players, callings):
    rank = {}
    for i, p in enumerate(players):
        rank[p] = i+1
    print(rank)
    for c in callings:
        sortedR = sorted(rank.items(), key=lambda x: x[1])
        # print(sortedR)
        index = sortedR.index((c, rank[c]))
        rank[sortedR[index-1][0]] += 1
        rank[c] -= 1


    return [x[0] for x in sorted(rank.items(), key=lambda x: x[1])]


print(solution(["mumu", "soe", "poe", "kai", "mine"],	["kai", "kai", "mine", "mine"]))