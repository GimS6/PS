# 2
# 문제: https://www.acmicpc.net/problem/2533

# 어떤 아이디어를 사회망 서비스에 퍼뜨리고자 할 때,
# 그래프에서 필요한 얼리 아답터*의 최소 수를 구하라
#  *얼리 아답터(early adaptor): 어떤 새로운 아이디어를
#                           먼저 받아들인 사람

import sys


N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    # 트리 구조 이므로 
    graph[u].append(v)
    graph[v].append(u)

count = 0
d = [[0, 0] for _ in range(len(graph))] # 0: 일반인, 1: 얼리 어답터
is_visited = [False] * len(graph)

# 루트 노드가 일반인인 경우:
#   루트 노드를 포함하여, 자식 노드들 안에서 최소 얼리 어답터 수(최적해)
#   d[i][0]
# 루트 노드가 얼리어답터인 경우:
#   루트 노드를 포함하여, 자식 노드들 안에서 최소 얼리 어답터 수(최적해)
#   d[i][1]

# 부모 노드가 일반인일 경우, 자식 노드는 얼리 어답터여야 한다.
# 부모 노드가 얼리 어답터일 경우, 자식노드가 얼리 어답터일 경우가 최적해라는 보장이 없음
#   - 자식 노드가 얼리 어답터일 경우와 아닐 경우 중 더 작은 값을 골라 다이내믹 리스트에 할당한다.
# d[i][0] += d[child][1]
# d[i][1] += min(d[child][1], d[child][0])

def dfs(root: int):
    is_visited[root] = True
    d[root][1] = 1

    for i in range(len(graph[root])):
        child = graph[root][i]

        if is_visited[child]:
            continue

        dfs(child)

        d[root][0] += d[child][1]
        d[root][1] += min(d[child][1], d[child][0])

dfs(1)

print(min(d[1][0], d[1][1]))