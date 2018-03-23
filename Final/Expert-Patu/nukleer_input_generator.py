from random import randint
from random import shuffle

print("olusturulacak input case sayisini giriniz:")

for i in range(int(input())):
    if i<10:
        out = open("input/input0" + str(i) + ".txt", "w")
    else:
        out = open("input/input" + str(i) + ".txt", "w")

    print(i," numarali input icin  M adet ulke sayisini sayisini girin:")
    M = int(input())

    print(i, " numarali input icin  N adet nukleer sayisini sayisini girin:")
    N = int(input())

    sinir = 10000000
    gensinir = 200000//M -1
    #print(gensinir)

    kok = M ** 0.5
    kok = kok // 1 + 1
    arttirma = sinir // kok - 1

    xSinir = arttirma
    ySinir = arttirma
    toplam = 0

    #ulke olusturucu

    print(M,file=out)
    for _ in range(M):
        if _ % 100 == 0:
            pass
            #print(_)
        merkezX = randint(xSinir - arttirma + 30, xSinir - 30)
        merkezY = randint(ySinir - arttirma + 30, ySinir - 30)
        #print("merkez x ve y", merkezX,merkezY)
        #print("sinir x ve y", xSinir, ySinir)

        xList = []
        yList = []

        ustAlt = randint(0,1)
        noktaX = merkezX
        noktaY = merkezY

        #print(noktaX,noktaY)
        xList.append(noktaX)
        yList.append(noktaY)

        #uste uzanan sekil
        if ustAlt == 0:
            #sag taraftaan yukari cikma

            while True:
                if (randint(0,99) == 99 and noktaX != merkezX and noktaY != merkezY) or noktaY+1+((ySinir-1-noktaY)//100+1) > ySinir - 1:
                    break
                if len(xList) >= gensinir:
                    break

                noktaX = randint(merkezX + 1,xSinir - 1)
                noktaY = randint(noktaY+1,noktaY+1+((ySinir-1-noktaY)//100+1))

                #print(noktaX,noktaY)
                xList.append(noktaX)
                yList.append(noktaY)

            #sol taraftan sagi inme
            #print("ikinci kisim")
            noktaX = randint(xSinir - arttirma + 1, merkezX - 1)
            kontrolx = noktaX
            kontroly = noktaY

            #print(noktaX,noktaY)
            xList.append(noktaX)
            yList.append(noktaY)
            while True:
                if (randint(0,99) == 99 and noktaX != kontrolx and noktaY != kontroly) or noktaY-1-((noktaY-1-merkezY)//100+1) < merkezY +1:
                     break
                if len(xList) >= gensinir:
                    break

                noktaX = randint(xSinir - arttirma + 1,merkezX -1)
                noktaY = randint(noktaY-1-((noktaY-1-merkezY)//100+1),noktaY-1)

                #print(noktaX,noktaY)
                xList.append(noktaX)
                yList.append(noktaY)
        #alta uzanan sekil
        else:
            #sol taraftan asagi inme
            while True:
                if (randint(0,99) == 99 and noktaX != merkezX and noktaY != merkezY) or noktaY-1-((noktaY-1-(ySinir-arttirma))//100+1) < ySinir - arttirma + 1:
                    break
                if len(xList) >= gensinir:
                    break

                noktaX = randint(xSinir - arttirma + 1, merkezX - 1)
                noktaY = randint(noktaY-1-((noktaY-1-(ySinir-arttirma))//100+1),noktaY-1)

                #print(noktaX,noktaY)
                xList.append(noktaX)
                yList.append(noktaY)

            #sag taraftan yukari cikma
            #print("ikinci kisim")
            noktaX = randint(merkezX + 1, xSinir-1)
            kontrolx = noktaX
            kontroly = noktaY

            #print(noktaX, noktaY)
            xList.append(noktaX)
            yList.append(noktaY)
            while True:
                if (randint(0,99) == 99 and noktaX != kontrolx and noktaY != kontroly) or noktaY+1+((merkezY-1-noktaY)//100+1) > merkezY - 1:
                     break
                if len(xList) >= gensinir:
                    break

                noktaX = randint(merkezX + 1,xSinir - 1)
                noktaY = randint(noktaY+1,noktaY+1+((merkezY-1-noktaY)//100+1))
                #print(noktaX,noktaY)
                xList.append(noktaX)
                yList.append(noktaY)

        #dosyaya datalari yazma
        #print("data yaziyom")
        print(len(xList),file=out)
        toplam += len(xList)
        for p in range(len(yList)):
            print(xList[p],yList[p],end=" ",file=out)
        print(file=out)

        #bir sonraki bolgeye gecme
        if xSinir + arttirma > sinir:
            xSinir = arttirma
            ySinir += arttirma
        else:
            xSinir += arttirma

    #roket olusturucu
    print(toplam)
    print(N,file=out)
    #print("roket olusturuyom")

    for _ in range(N):
        roketX = randint(0,sinir)
        roketY = randint(0,sinir)
        print(roketX,roketY,file=out)

