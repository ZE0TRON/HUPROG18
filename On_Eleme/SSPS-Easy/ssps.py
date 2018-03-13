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
            a.append(elem)
    return a

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0: return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i==0:
            return False
    return True

a=find_asals(100000)
print(a)
for x in a:
    if isPrime(x):
        continue
    print(x)

