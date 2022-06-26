MyFirstList = [3, 45, 56, 732]
print(MyFirstList)
print(type(MyFirstList))

list2 = ["hello", 24, True, 55.3]
print(list2)
print(type(list2))

list3 = ["How are you?", 55, MyFirstList]
print(list3)
print(type(list3))

x = [1, 2, 3, 4, 5, 6, 7] #[1, 2, 3, 4, 5, 6, 7]
print(x)

y = list(range(8)) #[0, 1, 2, 3, 4, 5, 6, 7]
print(y)

z = list(range(1, 8)) #[1, 2, 3, 4, 5, 6, 7]
print(z)

z2 = list(range(100, 120)) #[100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
print(z2)

w = list(range(100, 111, 2)) #il terzo valore indica lo step ovvero quanti numeri deve saltare [100, 102, 104, 106, 108, 110]
print(w)

w2 = list(range(100, 201, 10)) #[100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
print(w2)
print(len(w2))

#      0    1    2    3    4
#     -5   -4   -3   -2   -1
w3 = ["a", "b", "c", "d", "e"]
print(w3)
print(w3[-1])
print(w3[-3])

#Slicing
#           0    1    2    3    4    5    6    7    8    9
#          -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
my_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "J"]
print(my_list[:]) # Tutta la lista ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'J']
print(my_list[:7]) # Dall'inizio fino all'elemento in posiozione 7 escluso ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(my_list[2:]) # Dalla posizione 2 compreso fino alla fine ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'J']
#Equivalente
print(my_list[-8:-3]) # ['c', 'd', 'e', 'f', 'g']
print(my_list[2:7]) # ['c', 'd', 'e', 'f', 'g']
print(my_list[-8:7])
#Advance Slicing
print(my_list[2:9:2]) # il terzo numero indica lo step ['c', 'e', 'g', 'i']
print(my_list[::3]) # Dall'inizio saltando 3 valori ['a', 'd', 'g', 'J']