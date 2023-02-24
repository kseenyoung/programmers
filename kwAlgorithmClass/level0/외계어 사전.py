def solution(spell, dic):
    for word in dic:
        if len(word) == len(spell):
            for w in word:
                if w not in spell:
                    break
                spell.remove(w)
            else:
                return 1
    return 2


print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
