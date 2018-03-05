import math

import os
from time import time


def find_asals(N):
    a = []
    a.append(1)
    for elem in range(2, N):
        flag = True
        for i in range(2, math.ceil(math.sqrt(elem)) + 1):
            if (elem % i == 0):
                flag = False
        if (flag == True):
            a.append(elem - 1)
    return a

a = time()
inputs = os.listdir("./input")
for inp in inputs:
    inputfile = open("input/" + inp, "r")
    number = inp[5:]
    out = open("outputs/output" + number , "w+")
    print("su an " + number + " nolu outputu hazirliyorum... gecen sure: " + str(time() - a))

    N = int(inputfile.readline())
    dizi = list(map(int, inputfile.readline().strip().split(" ")))
    aranan = int(inputfile.readline())
    asallar = find_asals(N)
    i = 0
    while i < len(asallar):
        if (len(dizi) <= asallar[i]-1):
            print("Not Found",file=out)
            break
        if (dizi[asallar[i]-1] < aranan):
            nothing = 0
        elif (dizi[asallar[i]-1] == aranan):
            print("Found",file=out)
            break
        else:
            dizi = dizi[asallar[i-1]-1:asallar[i]-1]
            print(*dizi,file=out)
            i = 1
        i += 1
    print(time()-a)
