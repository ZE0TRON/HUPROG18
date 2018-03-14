from collections import defaultdict


def zeroer():
    return 0


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
        if (int(elem[K - i - 1]) == 0):
            Tubes[i][0].append(int(elem))
        elif (int(elem[K - i - 1]) == 1):
            Tubes[i][1].append(int(elem))
        elif (int(elem[K - i - 1]) == 2):
            Tubes[i][2].append(int(elem))
        elif (int(elem[K - i - 1]) == 3):
            Tubes[i][3].append(int(elem))
        elif (int(elem[K - i - 1]) == 4):
            Tubes[i][4].append(int(elem))
        elif (int(elem[K - i - 1]) == 5):
            Tubes[i][5].append(int(elem))
        elif (int(elem[K - i - 1]) == 6):
            Tubes[i][6].append(int(elem))
        elif (int(elem[K - i - 1]) == 7):
            Tubes[i][7].append(int(elem))
        elif (int(elem[K - i - 1]) == 8):
            Tubes[i][8].append(int(elem))
        elif (int(elem[K - i - 1]) == 9):
            Tubes[i][9].append(int(elem))
isUsed = defaultdict(zeroer)
notsolved = True
end = False
lastj = 9
sortedlist = []
score = 0
i = N - 1
maxlist = []
maxscore = -1
while (len(solution) != 0 and i > -1):
    k = i % K
    j = lastj
    not_found = True
    while (not_found):
        if (len(Tubes[k][j] > 0)):
            for elem in Tubes[k][j]:
                if isUsed[elem] == 0:
                    not_found = False
                    break
        if (j == 0):
            if (len(solution > 0)):
                i, j, isUsed, sortedlist, score = solution.pop()
            else:
                i = -1
                break
        elif (not_found):
            j -= 1
    score += i * j
    for p in range(1, len(Tubes[k][j])):
        isUsed[Tubes[k][j][p]] = 1
        sortedlist.append(Tubes[k][j][p])
        solution.append([i - 1, j, isUsed, sortedlist, score])
        isUsed[Tubes[k][j][p]] = 0
        sortedlist.pop()
    sortedlist.append(Tubes[k][j][0])
    isUsed[Tubes[k][j][0]] = 1
    if (i == 0):
        if (score > maxscore):
            maxscore = score
            maxlist = sortedlist
        if (len(solution) > 0):
            i, lastj, isUsed, sortedlist, score = solution.pop()
    else:
        i -= 1
print(maxscore, maxlist)
