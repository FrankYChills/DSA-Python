# Given an integer array nums and an integer k, return the kth largest element in the array (not distinct)
# basic approach of sorting the array and then getting element accordingly will be in O(nlogn) TC
# we have to do in O(n) TC
# use quick sort but eliminating half of the list acc to condition(quick select)

def findKthLargest(nums, k):
    # kth largest in sorted will be at -
    k = len(nums) - k

    def QuickSelect(l, r):
        swapPointer = l
        pivot = nums[r]
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[swapPointer] = nums[swapPointer], nums[i]
                swapPointer += 1
        # swap pivot so that elements smaller than pivot are on left side of it and greater elements are on right side
        nums[swapPointer], nums[r] = nums[r], nums[swapPointer]

        # check if swapPointer is less than or greater or if equal thats the answer
        if swapPointer > k:
            # the element will be at less index than the swapped pivot value index(swapPointer)
            return QuickSelect(l, swapPointer - 1)
        elif swapPointer < k:
            # element will be at greater index than swapPointer
            return QuickSelect(swapPointer + 1, r)
        else:
            # if k == swapPointer that means its the value coz its sorted
            print(nums[swapPointer])
            return nums[swapPointer]

    return QuickSelect(0, len(nums) - 1)


findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
