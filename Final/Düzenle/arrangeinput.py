import random
import string
import timeit

for i in range(1):

    print("dosya adi girin:")
    output = input()

    out = open("input/input" + output + ".txt", "w")

    tlen = int(input("kelime uzunlugunu girin: "))
    if(tlen>100000 or tlen<1):
        print("gecersiz tlen uzunlugu!")
    n = int(input("n sayisini girin: "))
    if(n<1 or n>600):
        print("gecersiz n sayisi!")

    start = timeit.default_timer()
    t = ''.join(random.sample(string.ascii_lowercase, tlen))
    print(t, file=out)
    print(n, file=out)
    stop = timeit.default_timer()
    print(output, "numarali input dosyasi hazirlandi. Calisma suresi(sn): ", stop - start)
