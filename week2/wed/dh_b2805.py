n, m = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0

left = 0
right = max(heights)
while left <= right:
    center = (right + left) // 2

    total_wood = 0
    for height in heights:
        if 0 < height - center:
            total_wood += (height - center)

    if m < total_wood:
        answer = center
        left = center + 1
    elif m > total_wood:
        right = center - 1
    else:
        answer = center
        break

print(answer)
