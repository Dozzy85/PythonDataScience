list1 = [1, 2, 3, 4, 5]
print(list1)

lista2 = list1
print(lista2)

lista3 = lista2.copy()
print(lista3)

lista4 =list(range(0, 20))
print(lista4)

cubi = []
for i in range(0,21):
    cubi.append(i**3)
print(cubi)

#List Comprehension
cubi1 = [i**3 for i in range(0,21)]
print(cubi1)

cubi2 = [(i, i**3) for i in range(0,21)]
print(cubi2)

cubi3 = [(i, i**3) for i in range(0,21) if i%2==0]
print(cubi3)

list1 = [2, 4, 6, 89, 9]
list2 = [3, 5, 6, 89, 6]
listMulti = []
for i in list1:
    for j in list2:
        listMulti.append((i, j))
print(listMulti)

list3 = [2, 4, 6, 89, 9]
list4 = [3, 5, 6, 89, 6]
listMulti1 = [(i, j) for i in list3 for j in list4]
print(listMulti1)