from math import sqrt
from math import ceil
from math import floor
def carpanSayisi(N):
    total=0
    c = sqrt(N)
    for i in range(1,ceil(c)):
        if(N%i==0):
            total+=1
    total*=2
    if(c-int(c)==0):
        total+=1
    return total


N = int(input())
total = 0
for i in range(1,N+1):
    total+=carpanSayisi(i)
print(total+1)
