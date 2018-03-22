import os

inputs = os.listdir("./input")
for inp in inputs:
    if inp == "input15.txt":
        inputfile = open("input/" + inp, "r")


        N = int(inputfile.readline())
        for i in range(N-1):
            inputfile.readline().strip().split(" ")


        dizi=list(inputfile.readline().strip().split(" "))

        out = open("input/"+inp , "a+")
        print(file=out)

        dizi[72952] = "107460"
        dizi[72951] = "57635"
        dizi[72950] = "60446"
        dizi[72953] = "110766"
        dizi[72954] = "91629"


        dizi[72955]="0"



        for el in dizi:
            print(el,end=" ",file=out)
