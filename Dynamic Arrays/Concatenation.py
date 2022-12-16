def concat(nums):
    newarr = [None] * 2 * len(nums)

    for i in range(len(nums)):
        newarr[i] = nums[i]
        newarr[i + len(nums)] = nums[i]
    print(newarr)
    return newarr


concat([1, 2, 3])
