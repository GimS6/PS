# 3

from collections import defaultdict
from itertools import product

def binary_search(number_list, length, target):
    answer = -1
    start = 0
    end = length - 1

    # 탐색 시작점이 끝점보다 크면 종료
    while start <= end:
        mid = (start + end) // 2

        if number_list[mid] == target:
            answer = mid
            # 검색한 값이 찾으려는 값보다 크거나 같으면 
            # 탐색 끝점을 중간점에서 1 낮춘 값으로 할당한다.
            end = mid - 1
        elif number_list[mid] > target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

def solution(info, query):
    # 지원자들은
    # 4가지 항목중 반드시 선택한다.
    #   1. 개발언어
    #   2. 지원 직군
    #   3. 지원 경력
    #   4. 소울푸드
    # and 코딩 테스트 점수
    # "개발언어 직군 경력 소울푸드 점수"

    # 개발팀에서 원하는 인재를 뽑기 위해
    # 특정 조건을 요구한다.
    # 조건: "조건" or "-"

    # [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 받은
    # 사람은 모두 몇 명인가?

    d = defaultdict(list)

    # 지원자 정보 데이터베이스화
    for i in range(len(info)):
        lang, job, career, food, score = info[i].split(" ")

        conditions = product(*[
            [lang, '-'], 
            [job, '-'], 
            [career, '-'], 
            [food, '-'],
        ])

        for c in conditions:
            d[c].append(int(score))

    # 점수표 정렬
    for key in d:
        score_list = d[key]
        d[key] = sorted(score_list)

    # 개발팀 요구 조건에 맞는 지원자 탐색
    answer = []
    for i in range(len(query)):
        q = query[i].replace(" and ", " ")
        lang, job, career, food, score = q.split(" ")

        if (lang, job, career, food) in d:
            score_list = d[(lang, job, career, food)]
            
            target_location = binary_search(score_list, len(score_list), int(score))
            if target_location == -1:
                answer.append(0)
                continue
            
            answer.append(len(score_list) - target_location)
        
        else:
            answer.append(0)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

answer = solution(info=info, query=query)
print(answer)