def min_coin_change(amount, coins):
    """
    Returns minimum number of coins to make amount
    n -> number of coins
    m -> amount
    Runtime Complexity: O(n * m)
    Auxiliary Space: O(m)

    >>> min_coin_change(51, [1, 15, 10])
    5
    """
    coins.sort()
    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
            else:
                break
    return dp[amount] if dp[amount] <= amount else -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
