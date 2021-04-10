#2
import sys

INF = sys.maxsize

def floyd_warshal(graph):

    for k in range(1, len(graph)):
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                if graph[i][j] > graph[i][k] + graph[j][k]:
                    graph[i][j] = graph[i][k] + graph[j][k]

    return graph


def solution(n, s, a, b, fares):
    answer = 0

    # 각 구간의 요금표를 생성한다.
    cost_graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(len(cost_graph)):
        cost_graph[i][i] = 0

    for f in fares:
        src, dst, cost = f
        cost_graph[src][dst] = cost
        cost_graph[dst][src] = cost

    cost_graph = floyd_warshal(cost_graph)

    costs = []
    for i in range(1, len(cost_graph)):
        costs.append(cost_graph[s][i] + cost_graph[i][a] + cost_graph[i][b])

    answer = min(costs)   

    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

answer = solution(n, s, a, b, fares)
print(answer)