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