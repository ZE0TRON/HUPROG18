import math


def find_asals(N):
    a = []
    a.append(1)
    for elem in range(2, N):
        flag = True
        for i in range(2, math.ceil(math.sqrt(elem)) + 1):
            if (elem % i == 0):
                flag = False
        if (flag == True):
            a.append(elem - 1)
    return a


N = int(input())
dizi = list(map(int, input().strip().split()))
aranan = int(input())
asallar = find_asals(N)
i = 0
while i < len(asallar):
    if (len(dizi) <= asallar[i]-1):
        print("Not Found")
        break
    if (dizi[asallar[i]-1] < aranan):
        nothing = 0
    elif (dizi[asallar[i]-1] == aranan):
        print("Found")
        break
    else:
        dizi = dizi[asallar[i-1]-1:asallar[i]-1]
        print(*dizi)
        i = 1
    i += 1
