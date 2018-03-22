import os

inputs = os.listdir("./input")
for inp in inputs:
    inputfile = open("input/" + inp, "r")
    number = inp[5:]
    out = open("abc/output" + number , "w+")
    print("digraph G{",file=out)
    N = int(inputfile.readline())
    dizi=[]
    for i in range(N-1):
        dizi.append(list(inputfile.readline().strip().split(" ")))
    deg = inputfile.readline().strip().split(" ")

    for dd in dizi:
        dd[0]=deg[int(dd[0])-1]+"-"+dd[0]
        dd[1] = deg[int(dd[1])-1] + "-" + dd[1]
        print('"'+dd[0]+'"'+' -> '+'"'+dd[1]+'"',file=out)
    print("}",file=out)

