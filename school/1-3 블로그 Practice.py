listA = [4, 6, 3, 1, 7, 8, 9, 2, 5]
listA.sort(reverse=True)
print(listA)

# [9, 8, 7, 6, 5, 4, 3, 2, 1]

# listS = 'Hello World'
# for i in listS:
#     print(i)

dic = {"name": "sina", "age": 25, "department": "software"}
sorted_dic = sorted(dic.items())

print(dic)
print(sorted_dic)

# {'name': 'sina', 'age': 25, 'department': 'software'}
# [('age', 25), ('department', 'software'), ('name', 'sina')]

tupleList = [('a', 3), ('e', 1), ('c', 9), ('b', 2), ('d', 0)]
sorted_tuple = sorted(tupleList, key=lambda x: x[0])
print(sorted_tuple)

# [('a', 3), ('b', 2), ('c', 9), ('d', 0), ('e', 1)]

#5로 나눈 몫과 나머지
alist = [1, 4, 6, 5, 10, 14, 40, 33, 9, 65, 90]

for i in alist:
    q, r = divmod(i, 5)
    print("%d의 (몫,나머지) : (%d,%d)" %(i, q, r))