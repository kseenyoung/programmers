# 풀이1 (30%)
def solution(today, terms, privacies):
    term = {}
    today = list(map(int, today.split(".")))
    result = []

    # 계약 유효 기간
    for ter in terms:
        t, m = ter.split()
        term[t] = m

    for i, privacy in enumerate(privacies):
        date, t = privacy.split()  # 날짜, 조건
        days = list(map(int, date.split(".")))  # 날짜 분류

        day = days[2] - 1
        month = days[1] + int(term[t])
        year = days[0]

        if day == 0:
            month -= 1
            day = 28
        if month > 12:
            temp = month // 12
            year += temp
            month = month % 12 if month % 12 != 0 else 1

        print(today, year, month, day)
        if today[0] > year:
            result.append(i + 1)
        elif today[1] > month:  # 연도가 같고 달이 작을 때
            result.append(i + 1)
        elif today[0] == year and today[1] == month and today[2] > day:  # 연도와 달이 같고 날이 작을 때
            result.append(i + 1)

    return result

# 풀이(참고)
def intTodate(date):
    year, month, day = list(map(int, date.split('.')))
    return (year*12*28) + (month*28) + day
def solution(today, terms, privacies):
    today = intTodate(today)
    result = []
    dic = {}
    for term in terms:
        t, d = term.split()
        dic[t] = int(d)*28

    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        privacyInt = intTodate(date) + dic[term]
        print(privacyInt, today)
        if privacyInt <= today:
            result.append(i+1)

    return result


print(solution("2022.05.19",	["A 6", "B 12", "C 3"],	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01",	["Z 3", "D 5"],	["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2020.01.02", ["A 1"], ["2020.01.02 A"]))