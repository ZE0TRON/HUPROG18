N = int(input())
hints = []
for i in range(N):
    sayi, rakam, yer = input().split(" ")
    rakam = int(rakam)
    yer = int(yer)
    hints.append([sayi, rakam, yer])
for i in range(1000):
    flag = True
    for elem in hints:
        counter = 0
        matched = 0
        numbers = []
        numbers.append(elem[0][0])
        numbers.append(elem[0][1])
        numbers.append(elem[0][2])
        for eleme in numbers:
            if (i < 100 and i > 9):
                p = "0" + str(i)
            elif (i < 10):
                p = "00" + str(i)
            else:
                p = str(i)
            if (eleme in p):
                counter += 1
        for j in range(3):
            if (numbers[j] == p[j]):
                matched += 1
        if (counter != elem[1] or matched != elem[2]):
            flag = False
    if (flag):
        print("Founnddd : ", p)
        break
