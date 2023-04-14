# 풀이(38.9% -> 66.7%)
def solution(ingredient):
    answer = '1231'
    result = ''.join([str(i) for i in ingredient])
    count = 0
    while answer in result:
        count += count(answer)  # 1->result.count(answer)
        result = result.replace(answer, '')
    return count

# 77.8%
def solution(ingredient):
    answer = '1231'
    result = ''.join([str(i) for i in ingredient])
    count = 0
    while answer in result:
        count += 1
        index = result.find(answer)
        result = result[:index] + result[index+4:]
        # print(count, result)
    return count

# 참고
def solution(ingredient):
    answer = []
    count = 0
    for i in ingredient:
        answer.append(i)
        if answer[-4:] == [1, 2, 3, 1]:
            count += 1
            for _ in range(4):
                answer.pop()  # 중요
    return count


# 재풀이 (66.7% ->
def solution(ingredient):
    hambuger = '1231'
    ingredient = ''.join([str(i) for i in ingredient])
    result = 0
    while hambuger in ingredient:
        result += ingredient.count(hambuger)
        ingredient = ingredient.replace(hambuger, '')
    return result