from collections import deque
import copy

# BFS 75%
def solution(tickets):
    graph = {}
    que = deque()
    dic = {}
    for t in tickets:
        graph[t[0]] = graph.get(t[0], []) + [t[1]]
        dic[(t[0], t[1])] = dic.get((t[0], t[1]), 0) + 1

    for c in graph:  # 각 간선 정렬
        graph[c].sort()
    for a in graph["ICN"]:
        dic1 = copy.deepcopy(dic)
        answer = ["ICN"]
        que.append(a)
        dic1[("ICN", a)] -= 1
        while que:
            now = que.popleft()
            answer.append(now)
            if now in graph:
                for c in graph[now]:
                    if dic1[(now, c)]:
                        dic1[(now, c)] = dic1[(now, c)] - 1
                        que.append(c)
                        break

        if len(answer)-1 == len(tickets):
            break

    return answer

# DFS(참고)
def solution1(tickets):
    country = {}
    answer = []
    stack = ["ICN"]
    for a, b in tickets:
        country[a] = country.get(a, []) + [b]

    for c in country:
        country[c].sort()

    while stack:
        s = stack[-1]
        if s not in country or len(country[s]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(country[s].pop())

    print(answer[::-1])


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution1([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution1([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))