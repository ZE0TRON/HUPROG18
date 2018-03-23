import os
inputs = os.listdir("./input")
for inp in inputs:
    inputfile = open("input/" + inp, "r")
    number = inp[5:7]
    out = open("output/output" + number + ".txt", "w")



