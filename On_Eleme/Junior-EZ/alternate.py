N = int(input())
hints = []
for i in range(N):
    sayi, rakam, yer = map(int, input().split(" "))
    hints.append([sayi, rakam, yer])
for i in range(100, 1000):
    flag = True
    for elem in hints:
        counter = 0
        matched = 0
        numbers = []
        numbers.append(str(elem[0])[0])
        numbers.append(str(elem[0])[1])
        numbers.append(str(elem[0])[2])
        for eleme in numbers:
            if (eleme in str(i)):
                counter += 1
        for j in range(3):
            if (numbers[j] == str(i)[j]):
                matched += 1
        if (counter != elem[1] or matched != elem[2]):
            flag = False
    if (flag):
        print("Founnddd : ", i)
        break
