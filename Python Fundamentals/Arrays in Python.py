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