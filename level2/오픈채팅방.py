def solution(record):
    dic = {}
    result = []
    for reco in record:
        alist = reco.split()
        if alist[0] == 'Enter':
            result.append((alist[1], 0))
            dic[alist[1]] = alist[2]
        elif alist[0] == 'Leave':
            result.append((alist[1], 1))
        elif alist[0] == 'Change':
            dic[alist[1]] = alist[2]

    return [dic[a]+"님이 들어왔습니다."if b == 0 else dic[a]+"님이 나갔습니다." for a, b in result ]


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))