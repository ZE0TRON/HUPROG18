from collections import defaultdict


def solve(m, P):
    return m ^ P


def generateNewKey():
    return 5


graph = defaultdict(list)
N, E = map(int, input().split(" "))
for i in range(E):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)
P, Q = map(int, input().split(" "))
for i in range(Q):
    d = input().split()
    a = int(d[0])
    a = solve(a, P)
    if (a == 1):
        b = int(d[1])
        b = solve(b, P)
        graph[b] = []
    if (a == 2):
        b = int(d[1])
        b = solve(b, P)
        for elem in graph[b]:
            graph[elem].remove(b)
        graph[b] = []
    if (a == 3):
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
