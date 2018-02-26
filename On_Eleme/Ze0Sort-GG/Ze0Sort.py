N = int(input())
K = int(input())
liste = input.split(" ")
Tubes = []
stack = []
solution = []
for i in range(K):
    Tubes.append([])
    for i in range(10):
        Tubes[i].append([])
for i in range(K):
    for elem in liste:
        if(int(elem[K-i-1])==0):
            Tubes[i][0].append(int(elem))
        elif(int(elem[K-i-1])==1):
            Tubes[i][1].append(int(elem))
        elif(int(elem[K-i-1])==2):
            Tubes[i][2].append(int(elem))
        elif(int(elem[K-i-1])==3):
            Tubes[i][3].append(int(elem))
        elif(int(elem[K-i-1])==4):
            Tubes[i][4].append(int(elem))
        elif(int(elem[K-i-1])==5):
            Tubes[i][5].append(int(elem))
        elif(int(elem[K-i-1])==6):
            Tubes[i][6].append(int(elem))
        elif(int(elem[K-i-1])==7):
            Tubes[i][7].append(int(elem))
        elif(int(elem[K-i-1])==8):
            Tubes[i][8].append(int(elem))
        elif(int(elem[K-i-1])==9):
            Tubes[i][9].append(int(elem))
notsolved = True
end = False
lastj=9
isNotOkey = True
while(notsolved):
    for i in reversed(range(N)):
        k=i%K
        j=lastj
        while(len(Tubes[i][j])==0):
            if(j==0):
                end =True
                break
            j-=1
        if(end):
            solution,i = stack.pop()
        isNotOkey = True
        while(isNotOkey):
            if(j<0):
                solution,i,j=stack.pop()
            lastj=j
            if(len(Tubes[i][j])>1):
                anotherIndex = 0
                while(Tubes[i][j][anotherIndex] in solution):
                    anotherIndex+=1
                for p in range(anotherIndex+1,len(Tubes[i][j])):
                    if(Tubes[i][j][p] not in solution):
                        stack.append([solution+Tubes[i][j][p],i+1,lastj])
                isNotOkey=False
                solution.append(Tubes[i][j][anotherIndex])
            j-=1
