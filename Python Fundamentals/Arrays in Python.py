import numpy as np

l = [2345, 27, 546, 215, -1234]
print(l)

a = np.array(l) #converte una lista in un array
print(a)

b = np.array(["12", "455", "63.3", "True", "abc"], dtype="<U32")
print(b)

l.pop()
print(l)

print(a.mean()) #calcola la media

#Slicing di array
print(a) #[ 2345    27   546   215 -1234]
print(a[2:]) #[  546   215 -1234]
print(b) #['12' '455' '63.3' 'True' 'abc']
print(b[2:4]) #['63.3' 'True']
print(b[0]) #12
print(b[:]) #['12' '455' '63.3' 'True' 'abc']
c = a.copy()
print(c) #[ 2345    27   546   215 -1234]
c[0] = 0
print(a) #[ 2345    27   546   215 -1234]
print(c) #[    0    27   546   215 -1234]