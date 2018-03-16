from random import randint
from collections import defaultdict


def zeroer():
    return 0


print("Kac adet input dosyasi olusturulacak?: ")

for i in range(int(input())):
    if i < 10:
        out = open("input/input0" + str(i) + ".txt", "w")
    else:
        out = open("input/input" + str(i) + ".txt", "w")

    ##print(i, "'ninci input dosyasi icin n sayisini girin:")
    n = 25  #randint(int(input()), int(input()))  #int(input())

    sayiList = []
    enbuyuk = str(
        randint(10**(len(str(n)) + 2) + 1, 10**(len(str(n)) + 3) - 1))
    randomness = randint(0, n - 1)

    basamak = len(enbuyuk)
    if (basamak // 2 > 3):
        kp = randint(3, basamak // 2)
    else:
        kp = basamak
    for j in range(n):
        if j == randomness:
            sayiList.append(enbuyuk)
            continue
        sayi = str(randint(1, 1000000))
        hehe = basamak - len(sayi)
        a = "0" * hehe
        a += sayi
        sayiList.append(a)
    #print(sayiList)
    #print(kp)
    #print(basamak)
    #cozum#
    N = n
    K = kp
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
            if (int(elem[len(elem) - i - 1])) == 0:
                Tubes[i][0].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 1):
                Tubes[i][1].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 2):
                Tubes[i][2].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 3):
                Tubes[i][3].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 4):
                Tubes[i][4].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 5):
                Tubes[i][5].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 6):
                Tubes[i][6].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 7):
                Tubes[i][7].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 8):
                Tubes[i][8].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 9):
                Tubes[i][9].append(int(elem))
    #isUsed = defaultdict(zeroer)
    notsolved = True
    end = False
    j = 9
    sortedlist = []
    score = 0
    i = N - 1
    maxlist = []
    maxscore = -1
    isStarted = True
    while (i > -1):
        isStarted = False
        k = i % K
        not_found = True
        everythingscool = False
        solutiontaken = False
        while (not_found):
            if (len(Tubes[k][j]) > 0):
                for elem in Tubes[k][j]:
                    #if isUsed[elem] == 0:
                    if elem not in sortedlist:
                        #print("Dude ", elem, " never used before")
                        not_found = False
                        #print("I am here bitch j = ", j)
                        everythingscool = True
            if (j == 0 and not_found):
                if (len(solution) > 0):
                    i, j, sortedlist, score = solution.pop()
                    solutiontaken = True
                else:
                    i = -1
                    everythingscool = False
                    #print("Breaking the habbit ? ")
                    not_found = False
            elif (not_found):
                j -= 1
            #print("Debugging bitch i = ", i, " j = ", j, " len(Tubes[k][j])",
            #      len(Tubes[k][j]), " isEveryythin cool ? ", everythingscool)
        if (i > -1 and not solutiontaken):
            score += i * j
            for p in range(1, len(Tubes[k][j])):
                #print("Then i am not here")
                if (Tubes[k][j][p] not in sortedlist):
                    sortedlist.append(Tubes[k][j][p])
                    solution.append([i - 1, j, sortedlist.copy(), score])
                    sortedlist.pop()
            if (Tubes[k][j][0] not in sortedlist):
                sortedlist.append(Tubes[k][j][0])
            if (i == 0):
                if (score > maxscore and len(sortedlist) == N):
                    maxscore = score
                    maxlist = sortedlist.copy()
                if (len(solution) > 0):
                    i, j, sortedlist, score = solution.pop()
                    solutiontaken = True
            else:
                i -= 1
                #print("Decreasing ? ")
        if (i < 0 and not solutiontaken):
            if (len(solution) > 0):
                #    print("Takin solution")
                i, j, sortedlist, score = solution.pop()
                solutiontaken = True
    if (maxscore != -1):
        print(maxscore, list(reversed(maxlist)), K)
