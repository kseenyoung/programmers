def solution(N, stages):
    players = len(stages)  # 사용자 수
    answer = []

    for stage in range(1, N + 1):  # 각 스테이지 별 실패율 파악
        notsolved = stages.count(stage)  # 해당 스테이지에 위치한 사용자 수
        # 해당 스테이지를 클리어한 사람(players)이 0이 아니라면 '비클리어/클리어' 가 실패율이 된다
        answer.append((notsolved / players, stage) if players != 0 else (0, stage))
        players -= notsolved  # 다음 스테이지는 해당 스테이지 비해결한 사람 제외

    # 실패율 -> 스테이지 번호 오름차순으로 정렬
    answer.sort(key=lambda x: (-x[0], x[1]))
    return [i[1] for i in answer]  # 정렬된 결과에서 스테이지 번호만 출력