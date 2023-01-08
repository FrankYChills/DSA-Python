# Only for ranged-inputs - bucket sort

def sortColors(nums):
    countArray = [0, 0, 0]
    for i in nums:
        countArray[i] += 1
    print(countArray)
    i = 0
    for j in range(len(countArray)):
        while countArray[j] > 0:
            nums[i] = j
            countArray[j] -= 1
            i += 1
    print(nums)


sortColors([2, 0, 2, 1, 1, 0])
