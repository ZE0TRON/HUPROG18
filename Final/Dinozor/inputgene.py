from random import randint
import sys

sys.setrecursionlimit(4000)

def olustur(node):
    global number
    global sinir
    if number == sinir:
        return 0
    randomness = randint(1, 100)

    if(number > 500):
        if randomness > 66:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 56:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 49:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 45:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 43:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        else:
            return 0;
    else:
        if randomness > 60:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 40:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 35:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 32:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        elif randomness > 30:
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out); olustur(number)
            if number == sinir: return 0
        else:
            return 0;

print("olusturulacak input case sayisini giriniz:")
n=int(input())
for i in range(n):
    print(i, " graph sinirini giriniz:")
    sinir = int(input())
    number = 1
    while (number != sinir):
        if i<10:
            out = open("input/input" + str(i+26) + ".txt", "w")
        else:
            out = open("input/input" + str(i+26) + ".txt", "w")
        print(sinir,file=out)
        number = 1
        olustur(1)

        ilk = [x for x in range(sinir)]
        son = [x for x in range(sinir)]
        sifiryer=0
        for kk in range(len(ilk)):
            lni=len(ilk)
            x=randint(0,lni-1)
            if(ilk[x]==0): sifiryer=kk
            print(ilk[x],end=" ",file=out)
            if(x==lni-1):
                ilk = ilk[:x]
            else:
                ilk=ilk[:x]+ilk[x+1:]
        print("\n", sifiryer ,file=out)
        """for _ in range(len(son)):
            lni=len(son)
            x=randint(0,lni-1)
            print(son[x],end=" ",file=out)
            if(x==lni-1):
                son = son[:x]
            else:
                son=son[:x]+son[x+1:]"""




