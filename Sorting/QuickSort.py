# passes 11/18 test cases on leetcode
# unstable sort
# time complexity - Worst - O(n^2) and average - O(nlogn) & SC - O(1)


def sortArray(nums):
    def QuickSort(arr, s, e):
        if e - s <= 0:
            return arr

        # take a pivot(taking last element here)
        pivot = arr[e]
        # index where swap needs to be happen
        swapPointer = s
        # loop till pivot(-1)
        for i in range(s, e):
            if arr[i] < pivot:
                # if ith value is less than pivot swap it with swapPointer value
                arr[swapPointer], arr[i] = arr[i], arr[swapPointer]
                swapPointer += 1
        # after one loop we have to swap pivot with swapPointer value which makes sure element less than pivot are on
        # left side of pivot and greater elements are on the right side
        # pivot is at e
        arr[swapPointer], arr[e] = arr[e], arr[swapPointer]
        # now index at which pivot is, is sorted so apply recursive quick sort at both left and right sides excluding
        # pivot
        # sort left side
        QuickSort(arr, s, swapPointer - 1)
        QuickSort(arr, swapPointer + 1, e)

        print(arr)
        return arr

    return QuickSort(nums, 0, len(nums) - 1)


sortArray([11, 12, 13, 14, 15, 16])
