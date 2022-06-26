import numpy as np
from numpy.random import randn

N = 100000
counter = 0

for i in randn(N):
    if(i > -1 and i < 1):
        counter += 1
answer = counter / N
print(answer)