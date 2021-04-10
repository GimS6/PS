#2

from itertools import product
from collections import defaultdict

def binary_search(number_list, length, target):
    answer = -1
    start = 0
    end = length - 1

    while start <= end:
        middle = (start + end) // 2

        if number_list[middle] == target:
            answer = middle
            end = middle - 1
        elif number_list[middle] > target:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    
    return answer

def solution(info, query):
    answer = []
    info_db = defaultdict(list)

    ## 지원자들의 정보를 다양한 케이스로 그룹화하여 저장
    for i in info:
        lang, job, career, food, score = i.split()

        p = product(*[[lang, '-'], [job, '-'], [career, '-'], [food, '-']])

        for case in p:
            info_db[case].append(int(score))

    for key in info_db:
        item = info_db[key]
        info_db[key] = sorted(item)

    for q in query:
        q = q.replace(' and ', ' ')
        lang, job, career, food, score = q.split()

        if (lang, job, career, food) in info_db:
            score_list = info_db[(lang, job, career, food)]

            target_index = binary_search(score_list, len(score_list), int(score))

            if target_index == -1:
                answer.append(0)
                continue   

            answer.append(len(score_list) - target_index)

        else:
            answer.append(0)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

answer = solution(info, query)
print(answer)