def solution(m, musicinfos):
    m=m.replace('C#','H')
    m=m.replace('D#','I')
    m=m.replace('F#','J')
    m=m.replace('G#','K')
    m=m.replace('A#','L')
    
    result = "(None)"
    for info in musicinfos:
        start,end,title,sound = info.split(',')
        hour1,min1 = start.split(':')
        hour2,min2 = end.split(':')
        time = (int(hour2)-int(hour1))*60 +(int(min2)-int(min1))
        
        sound=sound.replace('C#','H')
        sound=sound.replace('D#','I')
        sound=sound.replace('F#','J')
        sound=sound.replace('G#','K')
        sound=sound.replace('A#','L')
        sound = sound*(time//len(sound)) + sound[0:time%len(sound)]
        if m in sound:
            if result == "(None)":
                result = title
                timechecker = time
            
            else :
                if timechecker < time:
                    result = title
                    timechecker = time
    return result