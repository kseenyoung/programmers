# 풀이1 (56.3%)
def solution(players, callings):
    rank = {}
    for i, p in enumerate(players):
        rank[p] = i+1

    for c in callings:
        sortedR = sorted(rank.items(), key=lambda x: x[1])
        # print(sortedR)
        index = rank[c]-1
        rank[sortedR[index-1][0]] += 1
        rank[c] -= 1

    return [x[0] for x in sorted(rank.items(), key=lambda x: x[1])]

# 풀이(참고)
def solution(players, callings):
    dic = {p: i for i, p in enumerate(players)}
    dicIdx = {i: p for i, p in enumerate(players)}

    for c in callings:
        currIdx = dic[c]
        frontIdx = currIdx - 1

        frontPlayer = dicIdx[frontIdx]
        dic[frontPlayer], dic[c] = dic[c], dic[frontPlayer]
        dicIdx[frontIdx], dicIdx[currIdx] = dicIdx[currIdx], dicIdx[frontIdx]

    return [x[0] for x in sorted(dic.items(), key=lambda x: x[1])]


print(solution(["mumu", "soe", "poe", "kai", "mine"],	["kai", "kai", "mine", "mine"]))