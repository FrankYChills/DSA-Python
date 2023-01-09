# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guessNumber(n):
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        # if guess is higher
        if guess(mid) == -1:
            r = mid - 1
        # if guess is smaller
        elif guess(mid) == 1:
            l = mid + 1
        # guess is correct
        elif guess(mid) == 0:
            return mid

