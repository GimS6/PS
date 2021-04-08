# 1

import sys

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
# 서로 갈 수 없는 정점에 쓰이는 값
INF = sys.maxsize

def floydWarshall(n, dist):
    # 경유 지점
    for k in range(n): 
        # 출발 지점
        for i in range(n):
            # 도착 지점
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def printSolution(n, dist):
    for i in range(n):
        for j in range(n):
            value = dist[i][j]
            if(dist[i][j] == INF):
                value = "INF" 
            print(value,end=' ')
        print()
            

def solution(n, s, a, b, fares):
    graph = [[INF] * n for i in range(n)]

    for i in range(n):
        graph[i][i] = 0

     # 정점 수
    for x, y, c in fares:
        # 두 지점 간 택시요금은 방향에 관계없이 동일하다.
        graph[x-1][y-1] = c
        graph[y-1][x-1] = c


    # 모든 지점 사이의 예상 최저 택시요금
    dist = floydWarshall(n, graph)

    # 출발지에서 합승 구간까지, 합승 구간에서 a, b 각각의 최소 택시비 요금을 구한다.
    mins = INF
    for k in range(n):
        if mins > dist[s-1][k] + dist[k][a-1] + dist[k][b-1]:
            mins = dist[s-1][k] + dist[k][a-1] + dist[k][b-1]
        
    return mins


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

answer = solution(n, s, a, b, fares)
print(answer)
