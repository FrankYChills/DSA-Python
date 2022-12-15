# function to remove all the occurences of val in nums

def removeOccurance(nums, val):
    # k keeps track of number that is equal to val
    # whenever i isn't equal to val swap that with k and when i is k increment i
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
    print(nums, k)


removeOccurance([1, 1], 2)
