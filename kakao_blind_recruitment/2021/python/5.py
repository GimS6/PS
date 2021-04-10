#2

HOUR = 3600
MINUTE = 60

def to_sec(time_str):
    H, M, S = time_str.split(":")
    return int(H) * HOUR + int(M) * MINUTE + int(S) 

def conver_time_to_str(sec):
    h = sec // HOUR
    sec = sec % HOUR
    m = sec // MINUTE
    s = sec % MINUTE

    hour = '0' + str(h) if h < 10 else str(h)
    minute = '0' + str(m) if m < 10 else str(m)
    second = '0' + str(s) if s < 10 else str(s)

    return f'{hour}:{minute}:{second}'

def solution(play_time, adv_time, logs):
    answer = ''

    # 모두 초로 환산
    play_time_sec = to_sec(play_time)
    adv_time_sec = to_sec(adv_time)

    logs_time_start = []
    logs_time_end = []

    for log in logs:
        START, END = log.split("-")
        logs_time_start.append(to_sec(START))
        logs_time_end.append(to_sec(END))

    total_time = [0] * (play_time_sec+1)

    # 시청자들의 시청 시작 시각, 종료 시각을 표시한다.
    # 시청 시작 +1
    # 시청 종료 -1
    for i in range(len(logs)):
        total_time[logs_time_start[i]] += 1
        total_time[logs_time_end[i]] -= 1

    # 시청자들의 재생 구간 중복 개수를 표시한다.
    for i in range(1, play_time_sec+1):
        total_time[i] += total_time[i-1]

    # x부터 x+1까지의 누적 재생 시간을 표시한다.
    for i in range(1, play_time_sec+1):
        total_time[i] += total_time[i-1]

    print(len(total_time))

    good_time = 0
    max_time = 0
    for i in range(adv_time_sec-1, play_time_sec):
        
        if i >= adv_time_sec:
            if max_time < total_time[i] - total_time[i - adv_time_sec]:
                max_time = total_time[i] - total_time[i - adv_time_sec]
                good_time = i - adv_time_sec + 1
        else:
            if max_time < total_time[i]:
                max_time = total_time[i]
                good_time = i - adv_time_sec + 1

    answer = conver_time_to_str(good_time)

    return answer


play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]


answer = solution(play_time, adv_time, logs)
print(answer)
