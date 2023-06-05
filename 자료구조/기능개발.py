# 27.3%
import math
def solution(progresses, speeds):
    answer = []
    while speeds:
        result = 1
        temp = math.ceil((100-progresses[0])/speeds[0])
        days = temp if temp > 0 else 0
        flag = True
        for i in range(1, len(speeds)):
            progresses[i] += speeds[i]*days
            if progresses[i] >= 100 and flag:
                result += 1
            else:
                flag = False
        progresses = progresses[result:]
        speeds = speeds[result:]
        answer.append(result)
    return answer



# print(solution([93, 30, 55],	[1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))
print(solution([90, 90, 90, 90], [30, 1, 1, 1]))