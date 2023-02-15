def solution(participant, completion):
    #방법1
    # participant.sort()
    # completion.sort()
    #
    # for i, p in enumerate(participant):
    #     if i == len(participant)-1:
    #         return p
    #     if p != completion[i]:
    #         return p

    #방법1
    hash = {}
    answer = 0
    for p in participant:
        if p not in hash:
            hash[p] = 1
        else:
            hash[p] += 1
    for c in completion:
        hash[c] -= 1




#testcase
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))