# 내 풀이(20.8% -> 100%) k이상 발생시 즉시 메일을 보냄으로 이후 신고자는 받지 못하는 코드였었다.
def solution(id_list, report, k):

    user = {id: 0 for id in id_list}  # 유저 별 통보 받은 횟수
    score = {id: set() for id in id_list}  # 유저 별 신고한 사람

    for repo in report:
        a, b = repo.split()
        score[b].add(a)

    for sco in score:
        if len(score[sco]) >= k:
            for u in score[sco]:
                user[u] += 1

    return [s for s in user.values()]

print(solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"], 3))
