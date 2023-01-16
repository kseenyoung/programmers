# def solution(storey):
#     answer = 0
#     # if storey % 10 > 5:
#     #     n = 10 - storey % 10
#     #     answer += n
#     #     storey += n
#     # if (storey % 100) - (storey % 10) > 50:
#     #     n = 100 - (storey % 100) - (storey % 10)
#     #     answer += n
#     #     storey += n
#     i = 1
#     while storey // 10**i > 0:
#         if storey % 10**i > 5*i:
#             n = 10**i - (storey % 10**i)
#             answer += n
#             storey += n
#
#     answer += storey//100
#     storey %= 100
#     answer += storey//10
#     storey %= 10
#     answer += storey
#
#     return answer


#풀이
def solution(storey):
    if storey <= 1:
        return storey
    q, m = divmod(storey, 10)
    return min(solution(q) + m, solution(q+1) + (10-m))


print(solution(2554))