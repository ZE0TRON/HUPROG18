print("kaç tane input case:")

for i in range(int(input())):
    if i<10:
        out = open("input/input0" + str(i) + ".txt", "w")
    else:
        out = open("input/input" + str(i) + ".txt", "w")

    print(i," seker sayisini girin:")
    n = int(input())
    print(n,file=out)
