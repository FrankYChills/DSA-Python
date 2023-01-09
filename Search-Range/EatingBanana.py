def minEatingSpeed(piles, h):
    # a number k (k piles/hour) at which all piles can be eaten in one hour will be the max number in piles
    # but we have to find the minimum
    # min can be started with k=1(1 banana per hour)
    # so the range will be from 1 to k (max(piles))
    # depending on h hours given we can brute force from eating 1 banana from a pile in a hour to eating max(piles)
    # banana an hour and then returning the min rate
    # using binary search we can do ease this by eliminating half of numbers from range according to if the rate
    # (total hours at that rate) is low or high

    l, r = 1, max(piles)
    # lets say min eating rate an hour is the max(nums) at start
    minRate = r
    while l <= r:
        midRate = (l + r) // 2
        # calculate hour for the current rate
        totalHours = 0
        # check if thats slow or fast
        for pile in piles:
            # use math.ceil for uppper bound
            totalHours += math.ceil(pile / midRate)
        if totalHours <= h:
            # at currentRate all piles can be eaten within h hours so
            # set min to currRate
            minRate = min(minRate, midRate)
            # decrease r cause they can be eaten in lower rate
            r = midRate - 1
        else:
            # total hours exceeded given hours.we need greater rate than currRate
            l = midRate + 1
    return minRate
