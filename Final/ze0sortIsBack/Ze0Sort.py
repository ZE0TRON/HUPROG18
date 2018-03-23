Q = int(input())
for _ in range(Q):
    N = int(input())
    K = int(input())
    liste = input().rstrip().split(" ")
    Tubes = []
    stack = []
    solution = []
    for i in range(K):
        Tubes.append([])
        for k in range(10):
            Tubes[i].append([])
    for i in range(K):
        for elem in liste:
            if (int(elem[len(elem) - i - 1])) == 0:
                Tubes[i][0].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 1):
                Tubes[i][1].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 2):
                Tubes[i][2].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 3):
                Tubes[i][3].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 4):
                Tubes[i][4].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 5):
                Tubes[i][5].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 6):
                Tubes[i][6].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 7):
                Tubes[i][7].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 8):
                Tubes[i][8].append(int(elem))
            elif (int(elem[len(elem) - i - 1]) == 9):
                Tubes[i][9].append(int(elem))
    notsolved = True
    end = False
    j = 9
    sortedlist = []
    score = 0
    i = N - 1
    maxlist = []
    maxscore = -1
    isStarted = True
    while (i > -1):
        isStarted = False
        k = i % K
        not_found = True
        everythingscool = False
        solutiontaken = False
        while (not_found):
            if (len(Tubes[k][j]) > 0):
                for elem in Tubes[k][j]:
                    if elem not in sortedlist:
                        not_found = False
                        everythingscool = True
            if (j == 0 and not_found):
                if (len(solution) > 0):
                    i, j, sortedlist, score = solution.pop()
                    solutiontaken = True
                else:
                    i = -1
                    everythingscool = False
                    not_found = False
            elif (not_found):
                j -= 1

        if (i > -1 and not solutiontaken):
            score += i * j
            for p in range(1, len(Tubes[k][j])):
                if (Tubes[k][j][p] not in sortedlist):
                    sortedlist.append(Tubes[k][j][p])
                    solution.append([i - 1, j, sortedlist.copy(), score])
                    sortedlist.pop()
            if (Tubes[k][j][0] not in sortedlist):
                sortedlist.append(Tubes[k][j][0])
            if (i == 0):
                if (score > maxscore and len(sortedlist) == N):
                    maxscore = score
                    maxlist = sortedlist.copy()
                if (len(solution) > 0):
                    i, j, sortedlist, score = solution.pop()
                    solutiontaken = True
            else:
                i -= 1
        if (i < 0 and not solutiontaken):
            if (len(solution) > 0):
                i, j, sortedlist, score = solution.pop()
                solutiontaken = True
    if (maxscore != -1):
        print(maxscore)
        for elem1 in list(reversed(maxlist)):
            print(elem1, end=" ")
        print()
    else:
        print(-1)

