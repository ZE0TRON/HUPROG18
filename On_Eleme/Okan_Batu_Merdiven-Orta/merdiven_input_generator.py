from random import randint

print("kaç tane input case:"),

for i in range(int(input())):
    if i<10:
        out = open("input/input0" + str(i) + ".txt", "w")
    else:
        out = open("input/input" + str(i) + ".txt", "w")

    print(i," n sayisini girin:")
    n = int(input())
    maksimum=100
    print(n,file=out)

    for k in range(n):
        sayi = randint(1,maksimum)
        print(sayi, file=out, end=" ")