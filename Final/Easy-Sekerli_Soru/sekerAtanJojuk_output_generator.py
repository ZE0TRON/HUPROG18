from math import sqrt
from math import ceil
from math import floor

import os
from time import time

def carpanSayisi(N):
    total=0
    c = sqrt(N)
    for i in range(1,ceil(c)):
        if(N%i==0):
            total+=1
    total*=2
    if(c-int(c)==0):
        total+=1
    return total


a = time()
inputs = os.listdir("./input")
for inp in inputs:
    inputfile = open("input/" + inp, "r")
    number = inp[5:7]
    out = open("output/output" + number + ".txt", "w")
    print("su an " + number + " nolu outputu hazirliyorum... gecen sure: " + str(time() - a))

    N = int(inputfile.readline())
    total = 0
    for i in range(1,N+1):
        total+=carpanSayisi(i)
    print(total+1, file=out)


