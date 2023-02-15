import heapq

def solution(scoville, K):
    #쌤 풀이
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    count = 0
    while heap[0] < K:
        try:
            a = heapq.heappop(heap) + heapq.heappop(heap) * 2
        except:
            return -1
        heapq.heappush(heap, a)
        count += 1

    return count