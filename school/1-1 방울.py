def solution(bell):
    bell_l = len(bell)
    maxN = 0

    for i in range(bell_l):
        result = bell_l - i
        for j in range(bell_l - result):
            templist = bell[j:j+result]
            if templist.count(1) - templist.count(2) == 0:
                return result


    answer = 0
    return answer

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
