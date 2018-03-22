from random import randint
from random import shuffle

print("olusturulacak input case sayisini giriniz:")

for i in range(int(input())):
    if i<10:
        out = open("input/input0" + str(i) + ".txt", "w")
    else:
        out = open("input/input" + str(i) + ".txt", "w")

    print(i,"numarali input icin  n sayisini girin:")
    n = int(input())

    liste = []
    derinlik = 1
    nerdeyim = 1
    memory = [1]


    num = n
    derinlikLim = 0
    while num > 1:
        num /= 4
        derinlikLim +=1

    print(n,file=out)

    for _ in range(n):
        weight = randint(1,1000000)
        if memory[len(memory) - 1] == 5:
            if len(memory) == derinlikLim:
                memory.pop()
                while memory[len(memory) - 1] == 4:
                    memory.pop()
                memory[len(memory) - 1] += 1
                memory.append(1)
            else:
                memory[len(memory) - 1] = 1
                memory.append(1)

        data = [weight]
        data.append(len(memory))
        for i in memory:
            data.append(i)
        liste.append(data)
        memory[len(memory) - 1] += 1

    shuffle(liste)
    for elem in liste:
        for elem1 in elem:
            print(elem1,end=" ",file=out)
        print(file=out)






