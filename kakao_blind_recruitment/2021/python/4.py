# 3

import sys


INF = sys.maxsize

def floyd_warshal(graph):
    # k: 경유 노드
    for k in range(1, len(graph)):
        # i: 출발지 노드
        for i in range(1, len(graph)):
            # j: 목적지 노드
            for j in range(1, len(graph)):
                # 출발지에서 목적지로 바로 이동하는 값보다
                # 출발지 - 경유지 - 목적지 형태로 이동했을 때의 값이
                # 해당 값을 대입한다.
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph

def solution(n, s, a, b, fares):

    # a,b가 합승하여 적절하게 이동
    # 그래프
    # 모든 노드 사이의 최단 거리(최소 비용)을 찾는다.
    # 방향에 관계 없이 노드 사이의 비용은 동일하다.
    

    # 그래프의 값을 무한수로 초기화 한다.
    graph = [[INF] * (n+1) for _ in range(n+1)]

    # 주어진 노드 사이의 택시 비용을 그래프에 대입한다.
    for (c, d, f) in fares:
        graph[c][d] = f
        graph[d][c] = f

    # 그래프에서 노드 자기 자신에게 가는 비용은 없으므로
    # 0으로 초기화 한다.
    for i in range(len(graph)):
        graph[i][i] = 0

    # 그래프의 노드별 최단 거리를 모두 구해준다. - Floyd-Warshal 알고리즘
    graph = floyd_warshal(graph)

    costs = []
    # a와 b의 합승했을 때 최소 택시 비용을 구한다. 
    # i: 경유지
    for i in range(1, len(graph)):
        costs.append(graph[s][i] + graph[i][a] + graph[i][b])

    return min(costs)


n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

answer = solution(n=n, s=s, a=a, b=b, fares=fares)
print(answer)