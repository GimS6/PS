# 1

# d[root][0]: 팀장이 회의에 참석하지 않는 경우 최소 매출
# d[root][1]: 팀장이 회의에 참석하는 경우 최소 매출
# 팀장과 팀원 모두 참석하는 경우가 최솟값을 가질 수도 있다.
#   팀원이 참석했을 경우와 아닌 경우 중 최소값을 대입한다.
#   d[n][1] += min(d[child][0], d[child][1])

# 팀장이 참석하지 않는 경우 팀원이 반드시 참석해야 한다.
#   - 그룹원이 1명 이상 참석하는 경우
#       - d[n][0]을 업데이트 한다.

#   - 그룹원 중 아무도 참석하지 않는 경우
#       - cost가 가장 적은 그룹원 한 명을 보낸다.


from typing import List


MAX = 3000001
tree = [[] for _ in range(MAX)]
d = [[0,0] for _ in range(MAX)]
is_visited = [False] * MAX
sum_child = [0] * MAX

def dfs(root: int, sales: List[int]):
    is_visited[root] = True
    d[root][1] = sales[root-1]

    for i in range(len(tree[root])):
        child = tree[root][i]

        if is_visited[child]:
            continue

        dfs(child, sales)

        d[root][1] += min(d[child][0], d[child][1])

    tmp_sum = 0
    is_summed = False
    tmp_sum_list = []

    for i in range(len(tree[root])):
        child = tree[root][i]

        if d[child][0] > d[child][1]:
            is_summed = True
            tmp_sum += d[child][1]
        else:
            tmp_sum_list.append(d[child][1] - d[child][0])
            tmp_sum += d[child][0]

    if len(tree[root]) > 0:
        if is_summed:
            d[root][0] = tmp_sum
        else:
            d[root][0] = tmp_sum + min(tmp_sum_list)

def solution(sales, links):
    for a, b in links:
        tree[a].append(b)

    dfs(1, sales)

    return min(d[1][0], d[1][1])


sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

answer = solution(sales, links)
print(answer)