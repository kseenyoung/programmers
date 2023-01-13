#내풀이(75%)
def solution(n, lost, reserve):
    rlost = len(lost)
    for i in lost:
        if i - 1 in reserve:
            rlost -= 1
        elif i + 1 in reserve:
            rlost -= 1

    answer = n - rlost
    print(answer)


solution(5, [2, 4], [3])


#풀이1
def solution1(n, lost, reserve):
    #O(n)
    u = [1]*(n+2)
    for i in lost:
        u[i] -= 1
    for i in reserve:
        u[i] += 1
    for i in range(1, n+1):
        if u[i] == 2 and u[i-1] == 0:
            u[i-1:i+1] = [1, 1] #list 범위 및 대입 값 주의!!!
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1, 1]

    return n - u.count(0)


#풀이2
def solution2(n, lost, reserve):
    #reserve 수(k)가 학생 수(n)보다 현저히 작을 때 : O(klogk)
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    for i in r:
        if i-1 in l:
            l.remove(i-1)
        elif i+1 in l:
            l.remove(i+1)

    return n - len(l)

print(solution2(5, [2, 4], [1, 3, 5]))