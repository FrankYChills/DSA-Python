# Insertion Sort - Insert the element in an sorted array
# j+1 - unordered value to be inserted
# j - rightmost/biggest value in the sorted array
# stable sort - relative order of same value preserved | unstable sort - Relative order isn't preserved
# This is stable sort
# TC - O(n^2) SC - O(1)

def sortArray(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]:
            # perform swap and decrement j
            temp = nums[j + 1]
            nums[j + 1] = nums[j]
            nums[j] = temp
            j -= 1

    print(nums)
    return nums


sortArray([3, 8, 4, 5, 1])
