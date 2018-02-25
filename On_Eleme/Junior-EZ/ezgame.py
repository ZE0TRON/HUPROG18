import sys

def startt(L):
    global ihtimaller
    ihtimaller = [[0 for i in range(10)] for k in range(L)]

def solution(lnn):
    sayi=[]
    for i in range(lnn):
        sayi.append(ihtimaller[i].index(max(ihtimaller[i])))
    print("".join(map(str,sayi)))

def check(lnn,sn,sx,sy):
    if(sx<sy):
        pass
    elif not sx and not sy:
        for i in range(lnn):
            for k in range(lnn):
                ihtimaller[i][int(sn[k])] = -1
    elif sx and not sy:
        for i in range(lnn):
            for k in range(lnn):
                isn=int(sn[k])
                if i==k:
                    ihtimaller[i][isn] = -1
                else:
                    if ihtimaller[i][isn]==0:
                        ihtimaller[i][isn] = 2
    elif sx and sy:
        for i in range(lnn):
            for k in range(lnn):
                isnk = int(sn[k])
                if k!=i:
                    ihtimaller[i][isnk]=-1
                else:
                    if ihtimaller[i][isnk]!=-1:
                        ihtimaller[i][isnk]=3

def main():
    for _ in range(int(sys.stdin.readline().strip())):
        L,Q = map(int,sys.stdin.readline().strip().split(' '))
        startt(L)
        for __ in range(Q):
            templist = list(sys.stdin.readline().strip().split(' '))
            check(L,templist[0],int(templist[1]),int(templist[2]))
        solution(L)
if __name__ == "__main__":
    ihtimaller=[[]]
    main()
