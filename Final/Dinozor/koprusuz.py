import os
from collections import defaultdict

gra=defaultdict(list)


inputs = os.listdir("./input")
for inp in inputs:
    inputfile = open("input/" + inp, "r")
    out = open("sonIn/" + inp , "w")

    N = int(inputfile.readline())
    print(N,file=out)
    for i in range(N-1):
        dizi=list(inputfile.readline().strip().split(" "))
        gra[int(dizi[0])-1].append(int(dizi[1])-1)
        gra[int(dizi[1]) - 1].append(int(dizi[0]) - 1)
        print(dizi[0],dizi[1],file=out)

    deg = inputfile.readline().strip().split(" ")
    print(" ".join(deg),file=out)
    sifpo=int(inputfile.readline().strip())
    ch=True
    sw=0
    while ch:
        ch=False
        for i in range(len(gra[sifpo])):
            if(gra[sifpo][i]<sifpo):
                deg[sifpo],deg[gra[sifpo][i]]=deg[gra[sifpo][i]],deg[sifpo]
                sifpo = gra[sifpo][i]
                ch=True
                sw+=1
                break
    print(" ".join(deg),file=out)
