# 풀이1(42.8%)
def solution(keymap, targets):
    # 문자 당 가장 작은 횟수
    count = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k not in count or count[k] > i:  # 한 번도 만나지 않았거나 현재 위치가 저장했던 수보다 작을 때
                count[k] = i + 1
    print(count)
    # 입력할 문자열
    answer = []
    for tar in targets:
        result = 0
        for t in tar:
            if t in count:
                result += count[t]
            else:
                return [-1]
        answer.append(result)
    return answer

# 풀이2(100%)
def solution(keymap, targets):
    # 문자 당 가장 작은 횟수
    count = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k not in count or count[k] > i: #한 번도 만나지 않았거나 현재 위치가 저장했던 수보다 작을 때
                count[k] = i+1

    # 입력할 문자열
    answer = []
    for tar in targets:
        result = 0
        temp = True
        for t in tar:
            if t in count:
                result += count[t]
            else:
                temp = False
                answer.append(-1)
                break
        if temp:
            answer.append(result)
    return answer

# 재풀이(52% -> 100%) : target에서 타이핑할 수 없는 것이 하나라도 나오면 -1
def solution(keymap, targets):
    dic = {}
    result = []
    for key in keymap:
        for i, k in enumerate(key):
            if k not in dic:
                dic[k] = i + 1
            else:
                dic[k] = min(dic[k], i + 1)
    for target in targets:
        count = 0
        for t in target:
            if t in dic:
                count += dic[t]
            else:
                result.append(-1)
                break
        else:
            result.append(count)

    return result
