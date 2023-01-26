#내 풀이
# def solution(scoville, K):
#     answer = 0
#
#     scoville.sort()
#     while scoville[0] < K:
#         scoville[1] = scoville[0] + 2 * scoville[1]
#         scoville.pop(0)
#         answer += 1
#     return answer
#
#
# print(solution([1, 2, 3, 9, 10, 12], 7))

#풀이
import heapq
def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0

    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= k:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        mixed = min1 + 2 * min2
        heapq.heappush(scoville, mixed)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
