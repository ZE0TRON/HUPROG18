from random import randint

print("dosya adi girin:")
output = input()

out = open("input/input" + output + ".txt", "w")

print("n sayisini girin:")
n = int(input())
maksimum = 1800000000 // n

sayi = randint(0,maksimum)
print(n,file=out)
print(sayi,file=out,end=" ")
arananindex = randint(0,n-2)

for i in range(n-1):
    sayi += randint(0,maksimum)
    print(sayi, file=out, end=" ")
    if(i == arananindex):
        aranansayi = sayi
print(file=out)
print(aranansayi, file=out)

