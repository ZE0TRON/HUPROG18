import math

import os
from time import time


def find_asals(N):
    a = []
    a.append(1)
    for elem in range(2, N+1):
        flag = True
        for i in range(2, math.ceil(math.sqrt(elem)) + 1):
            if (elem % i == 0):
                flag = False
        if (flag == True):
            a.append(elem - 1)
    return a

def solve(arr,asals):
    i=0
    "print(asals,'asals')"
    lnA=len(asals)
    while i<lnA:
        if(arr[asals[i]]==aranan):
            return "Found"
        if(arr[asals[i]]>aranan):
            print(" ".join([str(x) for x in arr[asals[i - 1]:asals[i] + 1]]),file=out)
            return solve(arr[asals[i-1]:asals[i]+1],asals[:i])
        if(i+1==lnA):
            print(" ".join([str(x) for x in arr[asals[i]:]]),file=out)
            return solve(arr[asals[i]:],find_asals(len(arr[asals[i]:])))
        i+=1
    return "Not Found"

a = time()
inputs = os.listdir("./input")
for inp in inputs:
    inputfile = open("input/" + inp, "r")
    number = inp[5:]
    out = open("output/output" + number , "w+")
    print("su an " + number + " nolu outputu hazirliyorum... gecen sure: " + str(time() - a))

    N = int(inputfile.readline())
    dizi = list(map(int, inputfile.readline().strip().split(" ")))
    aranan = int(inputfile.readline())
    asallar = find_asals(N)
    print(solve(dizi, asallar), file=out)

    print(time()-a)
