#1

from collections import defaultdict
from itertools import product, combinations

def solution(orders, course):
    combi = defaultdict(int)
    s = set()

    # 가능한 코스메뉴 조합과 주문된 횟수를 구한다.
    for i in range(len(orders)):
        o = list(orders[i])
        # 주문 메뉴 사전순으로 정렬
        o.sort()

        s.add(orders[i])
        for j in range(len(course)):
            if len(o) < course[j]:
                continue

            c = tuple(combinations(o, course[j]))
            for k in range(len(c)):
                combi[c[k]] += 1

    max_combi_list = [0] * len(course)
    answer = []

    # 문자열 길이 조합 중에서 가장 많이 나온 것들을 추린다.
    for i in range(len(course)):
        max_combi = 1
        for c in combi: 
            combi_str = ''.join(c)
            if len(combi_str) == course[i]:
                if max_combi < combi[c]:
                    max_combi = combi[c]

        max_combi_list[i] = max_combi

    # 조합 개수별 가장 많이 나온 메뉴들을 뽑는다.
    for i in range(len(max_combi_list)):
        for c in combi:
            combi_str = ''.join(c)
            if len(combi_str) == course[i] and max_combi_list[i] >= 2 and combi[c] == max_combi_list[i]:
                answer.append(combi_str)
                
    return sorted(answer)


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

answer = solution(orders=orders, course=course)
print(answer)