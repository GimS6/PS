# 1

def solution(new_id):
    # 규칙에 맞지 않는 문자열
    # 규칙이 있다.
    # 규칙에 맞는 아이디 추천
    # 입력한 아이디와 유사해야 한다.
    # 길이 3 이상 15 이하
    # 알파벳 소문자, 숫자, '-', '_', '.'만 사용
    # '.'는 처음과 끝에 올 수 없다. 연속 사용 ㄴㄴ
    recomend_id = ''

    #1
    new_id = new_id.lower()

    #2
    for char in new_id:
        if not char.isalpha() and not char.isdigit() and char != '-' and char != '_' and char != '.':
            continue
        recomend_id += char
    #3
    for _ in range(len(recomend_id)):
        recomend_id = recomend_id.replace("..", ".")

    #4
    if recomend_id.startswith('.'):
        recomend_id = recomend_id[1:]
    if recomend_id.endswith('.'):
        recomend_id = recomend_id[:len(recomend_id)-1]

    #5
    if recomend_id == '':
        recomend_id += 'a'

    #6
    if len(recomend_id) >= 16:
        cut_unit = len(recomend_id) - 15
        recomend_id = recomend_id[:len(recomend_id) - cut_unit]
    if recomend_id.endswith('.'):
        recomend_id = recomend_id[:len(recomend_id)-1]

    #7
    if len(recomend_id) <= 2:
        while len(recomend_id) < 3:
            recomend_id += recomend_id[-1]

    return recomend_id


new_id = "...!@BaT#*..y.abcdefghijklm"

answer = solution(new_id=new_id)
print(answer)