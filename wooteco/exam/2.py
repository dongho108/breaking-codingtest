def time_convert(total_min):
    hour = str(total_min // 60)
    minute = str(total_min % 60)

    if int(hour) < 10:
        hour = "0" + hour
    if int(minute) < 10:
        minute = "0" + minute
    return hour + ":" + minute


def timer(start, end):
    start_arr = list(map(int, start.split(":")))
    end_arr = list(map(int, end.split(":")))
    return (end_arr[0] * 60 + end_arr[1]) - (start_arr[0] * 60 + start_arr[1])


def solution(log):
    total_min = 0
    i = 0
    while i < len(log):
        study_time = timer(log[i], log[i + 1])
        if 5 <= study_time:
            if 105 <= study_time:
                study_time = 105
            total_min += study_time
        i += 2
    return time_convert(total_min)


# print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))
print(solution(["01:00", "24:00"]))
# print(solution(["01:00", "03:00", "04:00", "06:00", "07:00", "09:00"]))