from itertools import combinations


def solution(nums):
    #풀이1(30%)
    # nCr = combinations(nums, len(nums) // 2)
    # result = 0
    # for n in nCr:
    #     result = max(result, len(set(n)))  # count아님
    # return result

    #풀이2
    count = len(nums) // 2
    nums = set(nums)
    return len(nums) if len(nums) <= count else count


# 풀이3
def solution(nums):
    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 0
        dic[n] += 1
    return min(len(dic), len(nums)//2)

