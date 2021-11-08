class Solution:
    def binary_search(self, arr, target, start, end, ans1, ans2):
        if arr and arr[0] == target and arr[-1] == target:
            return [0, len(arr)-1]
        if start > end:
            return [-1, -1]
        mid = (start + end) // 2
        if arr[mid] == target:
            if ans1<0:
                if mid == 0 or arr[mid-1] != target:
                    ans1 = mid
                if mid == len(arr)-1 or arr[mid+1] != target:
                    ans2 = mid
                if ans1>=0 and ans2>=0:
                    return [ans1, ans2]
                elif ans1>=0:
                    return self.binary_search(arr, target, mid+1, end, ans1, ans2)
                elif ans2>=0:
                    return self.binary_search(arr, target, start, mid-1, ans1, ans2)
                else:
                    i = 1
                    while mid-i>=0 and ans1<0:
                        if arr[mid-i] != target:
                            ans1 = mid-i+1
                        i += 1
                    j = 1
                    while mid+j<len(arr) and ans2<0:
                        if arr[mid+j] != target:
                            ans2 = mid+j-1
                        j += 1
                    if ans1 == -1:
                        ans1 = 0
                    if ans2 == -1:
                        ans2 = len(arr)-1
                    return [ans1, ans2]
            if ans2<0:
                if mid == 0 or arr[mid-1] != target:
                    ans1 = mid
                if mid == len(arr)-1 or arr[mid+1] != target:
                    ans2 = mid
                if ans1>=0 and ans2>=0:
                    return [ans1, ans2]
                elif ans1>=0:
                    return self.binary_search(arr, target, mid+1, end, ans1, ans2)
                elif ans2>=0:
                    return self.binary_search(arr, target, start, mid-1, ans1, ans2)
                else:
                    i = 1
                    while mid-i>=0 and ans1<0:
                        if arr[mid-i] != target:
                            ans1 = mid-i+1
                        i += 1
                    j = 1
                    while mid+j<len(arr) and ans2<0:
                        if arr[mid+j] != target:
                            ans2 = mid+j-1
                        j += 1
                    if ans1 == -1:
                        ans1 = 0
                    if ans2 == -1:
                        ans2 = len(arr)-1
                    return [ans1, ans2]
        if arr[mid] < target:
            return self.binary_search(arr, target, mid+1, end, ans1, ans2)
        if arr[mid] > target:
            return self.binary_search(arr, target, start, mid-1, ans1, ans2)

    def searchRange(self, nums, target):
        start, end = 0, len(nums)-1
        ans1, ans2 = -1, -1
        return self.binary_search(nums, target, start, end, ans1, ans2)