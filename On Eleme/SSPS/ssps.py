import math
def find_asals(N):
    a=[]
    for elem in (2,N):
        flag=True
        for i in range(2,math.ceil(math.sqrt(elem))+1):
            if(elem%i==0):
                flag=False
        if(flag==True):
            a.append(elem)
    return a        
N=int(input())
dizi = list(map(int,input().split()))
aranan=int(input())
asallar = find_asals(N)
for i in range(len(asallar)):
    if(dizi[asallar[i]]<aranan):
        nothing=0
    elif(dizi[asallar[i]]==aranan):
        print(True)
    else:
        dizi=dizi[asallar[i]:asallar[i-1]]
        print(*dizi)
        i=0
    if(len(dizi==0)):
        print(False)
