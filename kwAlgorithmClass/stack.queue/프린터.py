from collections import deque

def solution(priorities, location):
    # 내 풀이(실패)
    # que = deque()
    # for i, p in enumerate(priorities):  # 인덱스 번호와 함께 queue 구성
    #     que.append((i, p))
    #
    # alist = sorted(que, key=lambda x: -x[1])
    #
    # for i, a in enumerate(alist):
    #     if a[1] == location:
    #         return i
    #         break
    # else:
    #     return len(priorities)-1

    #풀이
    que = deque()
    for i, p in enumerate(priorities):
        que.append((i, p))
    priorities.sort(reverse=True)
    idx = 0
    answer = 0

    while que:
        document = que.popleft()
        if document[1] == priorities[idx]:  # 뽑아낸 값이 현재 최적값 이라면
            if document[0] == location:  # 인쇄할 값이 찾던 문서일 때
                return answer + 1
            idx += 1
            answer += 1
        else:
            que.append(document)



print(solution([1, 1, 9, 1, 1, 1],	0)     )