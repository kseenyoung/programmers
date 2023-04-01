def solution(survey, choices):
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    choice = [3, 2, 1, 0, 1, 2, 3]  # 점수표
    for i, c in enumerate(choices):
        if c > 4:
            dic[survey[i][1]] += choice[c - 1]
        elif c < 4:
            dic[survey[i][0]] += choice[c - 1]

    result = 'R' if dic['R'] >= dic['T'] else 'T'
    result += 'F' if dic['F'] > dic['C'] else 'C'
    result += 'J' if dic['J'] >= dic['M'] else 'M'
    result += 'A' if dic['A'] >= dic['N'] else 'N'

    return result