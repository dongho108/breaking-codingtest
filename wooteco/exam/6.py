def convert(time):
    if time[-2:] == "PM":
        return int(time[:-2]) + 12
    else:
        return int(time[:-2])


def over(start, end):
    over_time = 0
    if convert(start) < convert("6PM"):
        over_time += min(8.5, convert("6PM") - convert(start))
    if convert("1PM") < convert(end):
        over_time += min(5, convert(end) - convert("1PM"))
    return over_time


def solution(time, plans):
    answer = "호치민"

    for name, start, end in plans:
        over_time = over(start, end)
        if time - over_time < 0:
            break
        else:
            time -= over_time
            answer = name
    return answer


# over("11PM", "9AM")
print(solution(14, [["서울", "9AM", "8PM"]]))
# print(solution(3.5, [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]]))