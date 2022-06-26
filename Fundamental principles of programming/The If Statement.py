#---- -2 ---- -1 ----0 ---- 1 ---- 2 ----
import numpy as np
from numpy.random import rand

x = rand()
answer = None

if x > 1:
    answer = "Grater than 1"
else:
    answer = "Less than 1"
print(x)
print(answer)

#Nested Statements
if x > 1:
    answer = "Grater than 1"
else:
    if x >= -1:
        answer = "Between -1 and 1"
    else:
        answer = "Less than -1"
print(x)
print(answer)

#Chained Statements
if x > 1:
    answer = "Grater than 1"
elif x >= -1:
    answer = "Between -1 and 1"
else:
    answer = "Less than -1"
print(x)
print(answer)