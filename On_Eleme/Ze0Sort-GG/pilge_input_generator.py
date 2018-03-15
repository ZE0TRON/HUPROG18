from random import randint
from collections import defaultdict


def zeroer():
    return 0

print("Kac adet input dosyasi olusturulacak?: ")

for i in range(int(input())):
    if i<10:
        out = open("input/input0" + str(i) + ".txt", "w")
    else:
        out = open("input/input" + str(i) + ".txt", "w")

    print(i,"'ninci input dosyasi icin n sayisini girin:")
    n = int(input())


    sayiList = []
    enbuyuk = str(randint(10 ** (len(str(n))+2)+1,10 ** (len(str(n))+3) -1))
    randomness = randint(0,n-1)
    basamak = len(enbuyuk)
    k = randint(2,basamak//2)
    for j in range(n):
        if j == randomness:
            sayiList.append(enbuyuk)
            continue
        sayi = str(randint(1,n*1000-1))
        hehe = basamak - len(sayi)
        a = "0"*hehe
        a += sayi

        sayiList.append(a)
    print(sayiList)
    print(k)
    #cozum#

    N = n
    K = k
    liste = sayiList
    Tubes = []
    stack = []
    solution = []
    for i in range(K):
        Tubes.append([])
        for k in range(10):
            Tubes[i].append([])
    for i in range(K):
        for elem in liste:
            if (int(elem[K - i - 1]) == 0):
                Tubes[i][0].append(int(elem))
            elif (int(elem[K - i - 1]) == 1):
                Tubes[i][1].append(int(elem))
            elif (int(elem[K - i - 1]) == 2):
                Tubes[i][2].append(int(elem))
            elif (int(elem[K - i - 1]) == 3):
                Tubes[i][3].append(int(elem))
            elif (int(elem[K - i - 1]) == 4):
                Tubes[i][4].append(int(elem))
            elif (int(elem[K - i - 1]) == 5):
                Tubes[i][5].append(int(elem))
            elif (int(elem[K - i - 1]) == 6):
                Tubes[i][6].append(int(elem))
            elif (int(elem[K - i - 1]) == 7):
                Tubes[i][7].append(int(elem))
            elif (int(elem[K - i - 1]) == 8):
                Tubes[i][8].append(int(elem))
            elif (int(elem[K - i - 1]) == 9):
                Tubes[i][9].append(int(elem))
    isUsed = defaultdict(zeroer)
    notsolved = True
    end = False
    j = 9
    sortedlist = []
    score = 0
    i = N - 1
    maxlist = []
    maxscore = -1
    isStarted = True
    while (len(solution) != 0 or i > -1):
        isStarted = False
        k = i % K
        not_found = True
        everythingscool = False
        while (not_found):
            if (len(Tubes[k][j]) > 0):

                for elem in Tubes[k][j]:
                    if isUsed[elem] == 0:
                        not_found = False
                        #print("I am here bitch j = ", j)
                        everythingscool = True
                        break
            if (j == 0 and not_found):
                if (len(solution) > 0):
                    i, j, isUsed, sortedlist, score = solution.pop()
                    everythingscool = True
                else:
                    i = -1
                    everythingscool = False
                    break
            elif (not_found):
                j -= 1
            #print("Debugging bitch i = ", i, " j = ", j, " len(Tubes[k][j])",
            #      len(Tubes[k][j]), " isEveryythin cool ? ", everythingscool)
        if (everythingscool):
            score += i * j
            for p in range(1, len(Tubes[k][j])):
                #print("Then i am not here")
                isUsed[Tubes[k][j][p]] = 1
                sortedlist.append(Tubes[k][j][p])
                solution.append([i - 1, j, isUsed, sortedlist, score])
                isUsed[Tubes[k][j][p]] = 0
                sortedlist.pop()
            sortedlist.append(Tubes[k][j][0])
            isUsed[Tubes[k][j][0]] = 1
            if (i == 0):
                if (score > maxscore):
                    maxscore = score
                    maxlist = sortedlist
                if (len(solution) > 0):
                    i, j, isUsed, sortedlist, score = solution.pop()
            else:
                i -= 1
    print(maxscore, maxlist)






