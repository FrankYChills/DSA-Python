# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


def firstBadVersion(n):
    l, r = 1, n

    while l <= r:
        midVersion = (l + r) // 2
        # that means version before mid may be bad
        if isBadVersion(midVersion):
            # but if midVersion is the first bad version
            if not isBadVersion(midVersion - 1):
                return midVersion
            # else
            r = midVersion - 1
        # bad version will be definately after midVersion then
        else:
            l = midVersion + 1
