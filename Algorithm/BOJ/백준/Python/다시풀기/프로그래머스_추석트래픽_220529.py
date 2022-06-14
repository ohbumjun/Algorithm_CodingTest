# https://programmers.co.kr/learn/courses/30/lessons/17676  ---
#

def get_request_count_during_one_second(time, start_and_end_times): 
    # time을 기준으로 log 들이 몇개나 포함되어 있는가
    request_count = 0
    start_time = time
    end_time = time + 1000
    for start_and_end_time in start_and_end_times:
        # 다른 작업의 끝나는 시점이,
        # # 현재 작업 시작 시점보다 늦고
        # 혹은, 다른 작업의 시작 시점이,
        # # 현재 작업 끝나는 시점보다 빠르고

        # 여기에서 start_and_end_time[0] < end_time 에서, <= 을 하면 안된다 !
        # 왜냐하면, 1초라는 것은, 시작시간은 포함하면서 1초, 즉, end_time은 포함하지 않게 되는것이기 때문이다
        if start_and_end_time[1] >= start_time and start_and_end_time[0] < end_time:
            request_count += 1
    return request_count


def solution(lines):
    # 필요한 정보는, 각 로그들의 시작, 끝나는 시점
    # 로그들의 끝나는, 시작하는 시점 계산하기
    if len(lines) == 1:
        return 1
    answer = 0
    start_and_end_times = []
    for line in lines:
        _, time, duration = line.split()
        time_array = time.split(':')
        duration = float(duration.replace('s', '')) * 1000
        hour = int(time_array[0]) * 3600
        minute = int(time_array[1]) * 60
        sec = float(time_array[2])
        end_time = (hour + minute + sec) * 1000
        start_time = end_time - duration + 1
        start_and_end_times.append([start_time, end_time])
    for st_time, ed_time in start_and_end_times:
        s1 = get_request_count_during_one_second(st_time, start_and_end_times)
        s2 = get_request_count_during_one_second(ed_time, start_and_end_times)
        tmp = max(s1, s2)
        answer = max(tmp, answer)
    return answer
