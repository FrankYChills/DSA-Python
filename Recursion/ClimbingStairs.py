# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climbStairs(n):
    dp = [1] * (n + 1)
    for i in range(n - 2, -1, -1):
        dp[i] = dp[i + 1] + dp[i + 2]
    print(dp[0])
    return dp[0]


climbStairs(2)
