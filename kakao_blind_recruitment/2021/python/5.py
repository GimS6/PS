# 3

HOUR_SEC = 3600
MINUTE_SEC = 60

def to_sec(time_str: str):
    # HH:MM:SS
    H, M, S = time_str.split(":")
    return int(H)*HOUR_SEC + int(M)*MINUTE_SEC + int(S)

def sec_to_time_str(sec: int):
    h = sec // HOUR_SEC
    sec = sec % HOUR_SEC
    m = sec // MINUTE_SEC
    s = sec % MINUTE_SEC
  
    h_str = '0' + str(h) if h < 10 else str(h)
    m_str = '0' + str(m) if m < 10 else str(m)
    s_str = '0' + str(s) if s < 10 else str(s)
  
    return f'{h_str}:{m_str}:{s_str}'

def solution(play_time, adv_time, logs):
    # 동영상의 전체 재생 구간
    # 총 재생시간
    # 각 시청자들의 동영상 재생 구간
    #   - 시작 시각
    #   - 종료 시각
    # 최적의 공익광고 위치
        # 공익 광고는 모두 재생되어야 한다.
    # 시청자들의 누적 재생시간이 가장 많이 나오는 구간에
    # 공익광고를 삽입하자.

    # 초 단위로 적절한 광고 삽입을 해야 한다. 
    # 모든 시간대를 초 단위로 변경한다.
    play_time_sec = to_sec(play_time)
    adv_time_sec = to_sec(adv_time)

    # 로그에서 시작 시간과 종료 시간을 구분해 저장한다.
    logs_sec_start = []
    logs_sec_end = []
    for log in logs:
        START, END = log.split("-")
        logs_sec_start.append(to_sec(START))
        logs_sec_end.append(to_sec(END))

    # 시청자들의 누적 시청 시간을 저장할 배열을 만든다.
    total_time = [0] * (play_time_sec+1)

    # 시청자들의 시청 시작, 종료 시각을 표시한다.
    # 시청 시작 = +1
    # 시청 종료 = -1
    for i in range(len(logs)):
        total_time[logs_sec_start[i]] += 1
        total_time[logs_sec_end[i]] -= 1
    
    # 구간별 시청자 수를 표시한다.
    for i in range(1, play_time_sec):
        total_time[i] += total_time[i-1]

    # 구간별 누적 시청 시간을 표시한다.
    for i in range(1, play_time_sec):
        total_time[i] += total_time[i-1]

    # 최적 광고 삽입 시간을 구한다.
    max_time = 0
    answer = 0

    for i in range(adv_time_sec-1, play_time_sec):
        if i >= adv_time_sec:
            if max_time < total_time[i] - total_time[i - adv_time_sec]:
                max_time = total_time[i] - total_time[i - adv_time_sec]
                answer = i - adv_time_sec + 1
        else:
            if max_time < total_time[i]:
                max_time = total_time[i]
                answer = i - adv_time_sec + 1
   
    return sec_to_time_str(answer)


play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

answer = solution(
    play_time=play_time, 
    adv_time=adv_time, 
    logs=logs,
    )
print(answer)
