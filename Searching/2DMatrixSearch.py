# TC - O(log(m*n))

def searchMatrix(matrix, target):
    l, r = 0, len(matrix) - 1
    print(target)
    def binarySearch(nums):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return True
        return False

    while l <= r:
        mid = (l + r) // 2

        if target < matrix[mid][0]:
            r = mid - 1
        elif target > matrix[mid][-1]:
            l = mid + 1
        else:

            return binarySearch(matrix[mid])
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
