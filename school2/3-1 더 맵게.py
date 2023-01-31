import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        min1 = heapq.heappop(scoville)
        if not scoville:
            return -1
        min2 = heapq.heappop(scoville)
        mix = min1 + 2 * min2
        heapq.heappush(scoville, mix)
        answer += 1

    return answer
