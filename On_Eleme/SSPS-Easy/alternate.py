import math


def find_asals(N):
    a = []
    a.append(1)
    for elem in range(2, N+1):
        flag = True
        for i in range(2, math.ceil(math.sqrt(elem)) + 1):
            if (elem % i == 0):
                flag = False
        if (flag == True):
            a.append(elem - 1)
    return a

def solve(arr,asals):
    i=0
    "print(asals,'asals')"
    lnA=len(asals)
    while i<lnA:
        if(arr[asals[i]]==aranan):
            return "Found"
        if(arr[asals[i]]>aranan):
            print(arr[asals[i-1]:asals[i]+1])
            return solve(arr[asals[i-1]:asals[i]+1],asals[:i])
        if(i+1==lnA):
            print(arr[asals[i]:])
            return solve(arr[asals[i]:],find_asals(len(arr[asals[i]:])))
        i+=1
    return "Not Found"


N = int(input())
dizi = list(map(int, input().strip().split()))
aranan = int(input())
asallar = find_asals(N)
print(solve(dizi,asallar))


"""
13
3 40 52 97 99 129 172 172 192 224 455 458 862
192

11
1 2 3 4 5 6 7 8 9 10 11
8


11
1 3 5 6 10 21 32 43 56 123 125
44

11
1 5 7 8 10 13 15 16 18 20 32
16


10
1 2 3 4 5 6 7 8 9 10
10


"""
