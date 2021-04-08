# 1

HOUR = 3600
MINUTE = 60 

def to_sec(time_str):
    [H, M, S] = time_str.split(":")
    return int(H)*HOUR + int(M)*MINUTE + int(S)

def solution(play_time, adv_time, logs):
    answer = ''

    # 모든 시각을 초로 환산한다.

    # play_time을 초로 환산
    play_time_sec = to_sec(play_time)

    # adv_time을 초로 환산
    adv_time_sec = to_sec(adv_time)

    logs_start_sec = []
    logs_end_sec = []

    for log in logs:
        [START, END] = log.split("-")
        
        # logs[i]의 시작 시간을 초로 환산
        logs_start_sec.append(to_sec(START))

        # logs[i]의 종료 시간을 초로 환산
        logs_end_sec.append(to_sec(END))


    total_time = [0] * (play_time_sec + 1)

    # total_time[x] = x 시간에 시작된 재생 구간의 개수 - x 시각에 종료된 재생 구간의 개수
    for i in range(len(logs)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1
    
    # total_time[x] = 시간 x부터 x+1까지 1초 간의 구간을 포함하는 재생 구간의 개수  
    for i in range(1, play_time_sec+1):
        total_time[i] = total_time[i] + total_time[i-1]

    for i in range(1, play_time_sec+1):
        total_time[i] = total_time[i] + total_time[i-1]
        
    max_time = 0
    target_time = 0

    for i in range(adv_time_sec-1, play_time_sec):
        if i >= adv_time_sec:
            # 가장 많은 누적 시청이 일어난 구간마다 광고 삽입 시간을 업데이트 한다.
            if max_time < total_time[i] - total_time[i - adv_time_sec]:
                max_time = total_time[i] - total_time[i - adv_time_sec]
                target_time =  i - adv_time_sec + 1
        else:
            if max_time < total_time[i]:
                max_time = total_time[i]
                target_time =  i - adv_time_sec + 1
        

    hour =  '0' + str(target_time // HOUR) if (target_time // HOUR) < 10 else str(target_time // HOUR)
    target_time =  target_time % HOUR

    min =  '0' + str(target_time // MINUTE) if (target_time // MINUTE) < 10 else str(target_time // MINUTE)
    target_time = target_time % MINUTE
   
    sec =  '0' + str(target_time) if (target_time) < 10 else str(target_time)

    answer = hour + ':' + min + ':' + sec

    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

# expect = "01:30:59"
answer = solution(play_time, adv_time, logs)
print(answer)
