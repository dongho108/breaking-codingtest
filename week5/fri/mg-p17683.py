def separate_melody(melody_str):
    new_music = list()
    melody_list = list(melody_str)
    while melody_list:
        temp = melody_list.pop(0)
        if melody_list:
            if melody_list[0] == '#':
                melody_list.pop(0)
                new_music.append(temp+'#')
            else:
                new_music.append(temp)
        else:
            new_music.append(temp)
    return new_music

def solution(m, musicinfos):
    answer = []
    order = 0
    for item in musicinfos:
        order += 1
        music = item.split(',')
        if int(music[0][0:2]) < int(music[1][0:2]):
            time = (60-int(music[0][3:]))+(int(music[1][0:2])-(int(music[0][0:2])+1))*60+int(music[1][3:])
        else:
            time = int(music[1][3:])-int(music[0][3:])
        new_music = separate_melody(music[3])
        m_melody = separate_melody(m)
        if time < len(new_music):
            melody = new_music[:time]
        else:
            melody = new_music*(time//len(new_music)) + new_music[:(time%len(new_music))]
        melody_check = melody.copy()
        i, check_list = 0, []
        while melody_check:
            temp = melody_check.pop(0)
            if temp == m_melody[i]:
                check_list.append(temp)
                i += 1
                if m_melody == check_list:
                    answer.append((music[2], time, order))
                    break
            elif len(check_list) > 0:
                i, check_list = 0, []
                melody_check.insert(0, temp)
                continue       
    if len(answer) == 0:
        return '(None)'
    answer = sorted(answer, key=lambda x:(-x[1], x[2]))
    return answer[0][0]