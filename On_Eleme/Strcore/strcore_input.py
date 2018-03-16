import random
from random import randint
import string
import timeit

for i in range(1):

    print("dosya adi girin:")
    output = input()

    out = open("input/input" + output + ".txt", "w")

    n = int(input("kelime sayisini giriniz: "))
    print(n,file=out)

    start = timeit.default_timer()
    for i in range(n):
        xrange = randint(3,10)
        xstring = ''.join(random.sample(string.ascii_lowercase, xrange))
        print(xstring,file=out,end=" ")

    stop = timeit.default_timer()
    print(output, "numarali input dosyasi hazirlandi. Calisma suresi(sn): ", stop - start)

