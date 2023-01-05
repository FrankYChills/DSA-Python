# Stable or Unstable depends on Implementation
# TC - O(nlogn) SC - O(1)
# we are dividing array into two halves until it gets to 1
# so height will be logn and at each step O(n) operation takes place

def sortArray(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        sub_array1 = nums[:mid]
        sub_array2 = nums[mid:]

        # sort both subarrays
        sortArray(sub_array1)
        sortArray(sub_array2)

        i = j = k = 0

        # while there are elements in both sub arrays
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                nums[k] = sub_array1[i]
                i += 1
            else:
                nums[k] = sub_array2[j]
                j += 1
            k += 1
        # While there are elements only in subarray1
        while i < len(sub_array1):
            nums[k] = sub_array1[i]
            i += 1
            k += 1
        # while there are elements only in subarray2
        while j < len(sub_array2):
            nums[k] = sub_array2[j]
            j += 1
            k += 1

        print(nums)
        return nums

    else:
        return nums


sortArray([-1, 2, -8, -10])
