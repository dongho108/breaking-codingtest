import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    limit = [tuple(map(int, input().strip().split())) for _ in range(N)]
    yeon = [tuple(map(int, input().strip().split())) for _ in range(M)]

    lim_index = 0
    lim_sections, lim_speed = limit[0]
    yeon_sections = 0
    over = 0
    for yeon_section, yeon_speed in yeon:
        if yeon_sections + yeon_section <= lim_sections:
            if yeon_speed > lim_speed:
                over = max(over, yeon_speed - lim_speed)
            yeon_sections += yeon_section
        elif yeon_sections < lim_sections:
            if yeon_speed > lim_speed:
                over = max(over, yeon_speed - lim_speed)
            yeon_sections += yeon_section
            while lim_sections < yeon_sections:
                lim_index += 1
                lim_section, lim_speed = limit[lim_index]
                lim_sections += lim_section
                if yeon_speed > lim_speed:
                    over = max(over, yeon_speed - lim_speed)
        else:
            yeon_sections += yeon_section
            while lim_sections < yeon_sections:
                lim_index += 1
                lim_section, lim_speed = limit[lim_index]
                lim_sections += lim_section
                if yeon_speed > lim_speed:
                    over = max(over, yeon_speed - lim_speed)
    print(over)
