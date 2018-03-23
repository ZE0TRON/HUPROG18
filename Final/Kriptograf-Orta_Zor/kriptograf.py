from collections import defaultdict


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


graph = defaultdict(list)
N, E = map(int, input().split(" "))
for i in range(E):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)
P, Q, U, K = map(int, input().split(" "))
for i in range(Q):
    d = input().split()
    a = int(d[0])
    a = solve(a, P)
    if (a == 1):
        b = int(d[1])
        b = solve(b, P)
        graph[b] = []
    elif (a == 2):
        b = int(d[1])
        b = solve(b, P)
        c = int(d[2])
        c = solve(c, P)
        graph[b].append(c)
        graph[c].append(b)
    P = generateNewKey()
M = int(input())
M = solve(M, P)
print(M)
