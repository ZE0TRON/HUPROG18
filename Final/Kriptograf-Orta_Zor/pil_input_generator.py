from collections import defaultdict
from random import randint
import sys

sys.setrecursionlimit(4000)

def solve(m, P):
    return m ^ P


def fastModularExp(a, b):
    result = 1
    a = a % K
    while b > 0:
        if (b % 2 == 1):
            result = (result * a) % K
        b = b >> 1
        a = (a * a) % K
    return result


def generateNewKey():
    nodes = []
    for elem in graph.keys():
        if (len(graph[elem]) % U == 0):
            nodes.append(elem)
    total = sum(nodes)
    key = 0
    for i in range(len(nodes)):
        deger = total - nodes[i]
        key = (key + fastModularExp(nodes[i], deger)) % K
    return key


def olustur(node):
    global number
    global sinir
    global graph
    if number == sinir:
        return 0
    randomness = randint(1, 100)

    if(number > 500):
        if randomness > 66:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        elif randomness > 56:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        elif randomness > 49:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        elif randomness > 45:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        elif randomness > 43:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        else:
            return 0;
    else:
        if randomness > 60:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        elif randomness > 40:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        elif randomness > 35:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        elif randomness > 32:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        elif randomness > 30:
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
            number += 1; print(str(node) + " " + str(number), file=out);graph[node].append(number);graph[number].append(node); olustur(number)
            if number == sinir: return 0
        else:
            return 0;

print("olusturulacak input case sayisini giriniz:")

for i in range(int(input())):
    print(i, " graph sinirini(minimum 5) giriniz:")
    sinir = int(input())
    number = 1
    if i < 10:
        out1 = open("output/output0" + str(i) + ".txt", "w")
    else:
        out1 = open("output/output" + str(i) + ".txt", "w")
    while (number != sinir):
        if i < 10:
            out = open("input/input0" + str(i) + ".txt", "w")
        else:
            out = open("input/input" + str(i) + ".txt", "w")
        print(sinir, sinir * 4, file=out)
        graph = defaultdict(list)
        number = 1
        olustur(1)
    node = sinir
    while sinir <= node*4:
        sinir += 1

        while True:
            a = randint(1,node-1)
            b = randint(1,node-1)
            if a != b:
                patladin = False
                for elem in graph[a]:
                    if elem == b:
                        patladin = True
                        break
                if not patladin:
                    break

        graph[a].append(b)
        graph[b].append(a)
        print(str(a) + " " + str(b), file=out)

    P = randint(1,1000)

    Q = randint(node//4 + 1, node//2 + 2)
    U = randint(1,10)
    K = randint(1,node*400)
    print(P, Q, U, K, file=out)
    N = node
    slinenler = [0]


    for i in range(Q):
        a = randint(1, 2)
        b = randint(1, N - 1)
        c = randint(1, N - 1)
        while b == c or b in slinenler:
            b = randint(1, N - 1)
            c = randint(1, N - 1)
        if (a == 1):
            a = solve(a, P)
            graph[b] = []
            b = solve(b, P)
            print(str(a) + " " + str(b),file=out)
        elif (a == 2):
            a = solve(a, P)
            graph[b].append(c)
            graph[c].append(b)
            b = solve(b, P)
            c = solve(c, P)
            print(str(a) + " " +str(b) + " " + str(c),file=out)
        P = generateNewKey()
    M = randint(0, N * 100)
    print(M,file=out1)
    M = solve(M, P)
    print(M,file=out)