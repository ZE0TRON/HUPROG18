import random
from random import randint
import string

print("dosya adi girin:")
output = input()

out = open("input/input" + output + ".txt", "w")

n = int(input("kelime sayisini giriniz: "))
print(n,file=out)

for i in range(n):
    xrange = randint(3,10)
    xstring = ''.join(random.sample(string.ascii_lowercase, xrange))
    #xstring = ''.join(random.choice(string.lowercase) for x in range(xrange))
    print(xstring,file=out,end=" ")


