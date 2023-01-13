# 내가 구현한 것(틀림)
# bell = [1,2,1,1,1,2,2,1]
# bell_l = len(bell)
# maxN = 0
#
# for i in range(bell_l):
#     result = bell_l - i
#     for j in range(bell_l - result):
#         templist = bell[j:j + result]
#         if templist.count(1) - templist.count(2) == 0:
#             print(result)
#             exit()
#
# answer = 0
# print(answer)


#풀이
from itertools import accumulate
def solution(bell):
    start = {}
    end = {}

    for i, x in enumerate(accumulate([0] + [1 if bell[a] == 2 else -1 for a in range(len(bell))])):
        if x not in start:
            start[x] = i
        end[x] = i

    return max(end[x] - start[x] for x in end)
