def solution(nums1, nums2):
    nums3 = []
    inx1, inx2 = 0, 0
    while inx1 < len(nums1) and inx2 < len(nums2):
        if nums1[inx1] < nums2[inx2]:
            nums3.append(nums1[inx1])
            inx1 += 1
        elif nums1[inx1] > nums2[inx2]:
            nums3.append(nums2[inx2])
            inx2 += 1
        else:
            nums3.append(nums1[inx1])
            nums3.append(nums2[inx2])
            inx1 += 1
            inx2 += 1

    if inx1 == len(nums1):
        nums3 += nums2[inx2:]
    elif inx2 == len(nums2):
        nums3 += nums1[inx1:]

    if len(nums3) % 2 == 1:
        return float(format(nums3[len(nums3) // 2], ".5f"))
    else:
        n1 = nums3[len(nums3) // 2]
        n2 = nums3[len(nums3) // 2 - 1]
        return float(format((n1 + n2) / 2, ".5f"))


print(solution([], [2, 3]))
# print(solution([1, 3], [2]))
# print(solution([1, 2], [3, 4]))
# print(solution([0, 0], [0, 0]))
# print(solution([], [1]))
# print(solution([2], []))