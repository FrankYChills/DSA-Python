def removedups(nums: int):
    print(f"Array before operation {nums}")
    if len(nums) < 2:
        print(nums)
        return len(nums)
    # nums[0] is sorted already
    l, r = 1, 1
    while r < len(nums):

        while r < len(nums) and nums[r] == nums[r - 1]:
            r += 1
        if r >= len(nums):
            print(f"Array After operation {nums}")
            print(f"{l} unique numbers in array")
            return l
        nums[l] = nums[r]
        l += 1
        r += 1
    print(f"Array After operation {nums}")
    print(f"{l} unique numbers in array")

    return l


removedups([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

# Method - Two Pointers
# Key - Take two pointers left and right.Left increments by one when replace happens and right increments until r-1 and r are same.When right goes out og bound we return left.
# We are placing all unique elements in first l positions.
