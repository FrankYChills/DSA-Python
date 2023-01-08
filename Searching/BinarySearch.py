# works only for sorted array
# TC - O(logn) cause we are eliminating half of the array in each ops

def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            return mid
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
