# 1

import itertools

def firsetOccurance(numbers, length, searchnum):
    # 변수 선언
    # 검색된 번호가 목록에 없는 경우 -1을 반환하고 start와 end도 초기화
    answer = -1
    # 탐색 시작점
    start = 0
    # 탐색 끝점
    end = length - 1

    # 검색된 번호의 가장 낮은 위치를 찾을 때까지 실행되는 반복문
    # 목록에 번호가 없는 경우 or 종료 지점이 시작 지점과 같을 때 중단됨
    while start <= end:
        # 중간 지점을 초기화 한다.
        # 시작점과 끝점의 중간값을 사용한다.
        middle = (start + end) // 2

        # 검색된 번호가 찾는 번호와 같을 경우
        if numbers[middle] == searchnum:
            answer = middle
            end = middle - 1
        # 검색된 번호가 찾는 번호보다 클 경우
        # 찾으려는 점수 이상을 찾으므로 이 조건에 해당할 때도
        # answer 값에 검색된 번호의 위치를 넣는다.
        elif numbers[middle] > searchnum:
            answer = middle
            end = middle - 1
        # 검색된 번호가 찾는 번호보다 작을 경우
        else:
            start = middle + 1

    return answer


def solution(info, query):
    groups = {}

    for s in info:
        spl = s.split(" ")
        items = [[spl[0], '-'], [spl[1], '-'], [spl[2], '-'], [spl[3], '-']]
        
        # cartesian product
        tuples = list(itertools.product(*items))

        # 그룹화 dict{ <조건>: [점수, ...]}
        for prod in tuples:
            if prod in groups:
                groups[prod].append(int(spl[4]))
            else:
                groups[prod] = [int(spl[4])]

    # 점수 정렬
    for key in groups:
        item = groups[key]
        groups[key] = sorted(item)

    # 조건에 맞는 지원자 탐색
    answer = []
    for q in query:
        accord = 0
        spl = q.split(" and ")
        [sf, score] = spl[3].split(" ")
        
        condition = (spl[0], spl[1], spl[2], sf)

        # print(f'{condition}, {score}')
        # 해당 조건을 찾는다.
        if condition in groups:
            scoreList = groups[condition]
            # 해당 점수 이상인 조건을 찾는다.
            # print(f'condition:{condition}, score:{score}, scoreList:{scoreList}')
            result = firsetOccurance(scoreList, len(scoreList), int(score))
            if result != -1:
                accord = len(scoreList) - result

        answer.append(accord)

    return answer

# 4가지 항목 선택
#   1. 언어
#   2. 직군
#   3. 경력
#   4. 소울푸드

# 지원서 info, 조건 질문 query가 주어질 때,
# 각 조건에 해당하는 인원 수를 배열에 담아 반환하라.


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

result = solution(info, query)
print(result)