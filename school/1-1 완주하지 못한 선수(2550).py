participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


hash = dict()
for p in participant:
    if p in hash:
        hash[p] += 1
    else:
        hash[p] = 1

for c in completion:
    hash[c] -= 1

for key, value in hash.items():
    if value == 1:
        print(key)
        exit()

# def solution(participant, completion):
#
#     for i in completion:
#         if i in participant:
#             participant.remove(i)
#
#     return participant[0]