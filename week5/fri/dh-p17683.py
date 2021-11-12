import math


def timesub(after, before):
    ahour, aminute = after.split(":")
    bhour, bminute = before.split(":")
    a = int(ahour) * 60 + int(aminute)
    b = int(bhour) * 60 + int(bminute)
    return a - b


def replacesharp(sheet):
    sheet = sheet.replace('C#', 'c')
    sheet = sheet.replace('D#', 'd')
    sheet = sheet.replace('E#', 'e')
    sheet = sheet.replace('F#', 'f')
    sheet = sheet.replace('G#', 'g')
    sheet = sheet.replace('A#', 'a')
    sheet = sheet.replace('B#', 'b')
    return sheet


def solution(m, musicinfos):
    answer = []
    m = replacesharp(m)
    music = []

    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        musiclen = timesub(info[1], info[0])
        musicname = info[2]
        musicsheet = replacesharp(info[3])
        musicsheet = musicsheet * (math.ceil(musiclen / len(musicsheet)))
        musicsheet = musicsheet[:musiclen]
        music.append((musicname, musicsheet))

    for name, sheet in music:
        if sheet.find(m) != -1:
            if not answer:
                answer = [name, len(sheet)]
            elif answer[1] < len(sheet):
                answer = [name, len(sheet)]

    if answer:
        return answer[0]
    else:
        return "(None)"


# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("ABCDEFG", ["13:00,13:05,WORLD,ABCDEF", "13:00,13:05,WORLD,ABCDEF"]))