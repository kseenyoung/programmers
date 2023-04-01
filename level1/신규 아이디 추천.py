import re
# 풀이1 (26.9%) -> 풀이2 (참고)
def solution(new_id):
    # 1
    # result = ''
    # for n in new_id:
    #     if n.isupper():
    #         result += n.lower()
    #     else:
    #         result += n
    result = new_id.lower()

    # 2
    # answer = ''
    # for r in result:
    #     if r.isdigit() or r.islower() or r == '-' or r == '.' or r == '_':
    #         answer += r
    p = re.compile('[a-z0-9-_.]')
    answer = ''.join(p.findall(result))

    # 3
    # answer = answer.replace("..", ".")
    while '..' in answer:  # point
        answer = answer.replace("..", '.')

    # 4
    answer = answer[:-1] if answer[-1] == '.' else answer
    if answer != '' and answer[0] == '.':
        answer = answer[1:]

    # 5
    answer = 'a' if answer == '' else answer

    # 6
    answer = answer[:15] if len(answer) > 15 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    # 7
    if len(answer) < 3:
        count = 3 - len(answer)
        answer += answer[-1] * count

    return answer



print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("123_.def"))
print(solution("=.="))
print(solution("abcdefghijklmn.p"))
print(solution("...abcdefghijklmn....p"))