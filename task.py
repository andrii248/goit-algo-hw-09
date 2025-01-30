def find_coins_greedy(amount):
    # Available nominations of coins
    coins = [50, 25, 10, 5, 2, 1]
    change = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Number of coins
            change[coin] = count
            amount -= coin * count  # Remaining amount

    return change


amount = 648
greedy_result = find_coins_greedy(amount)
print(f"Change for {amount}: {greedy_result}")


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]  # Available coins
    dp = [float("inf")] * (amount + 1)  # Initialize DP table with infinity
    dp[0] = 0  # Base case
    coin_used = [-1] * (amount + 1)  # Store which coin was used

    # Compute the minimum coins needed for each amount from 1 to 'amount'
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:  # If using this coin reduces the total count
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin  # Store the coin used

    # Backtrack to find the coin combination
    if dp[amount] == float("inf"):
        return {}  # No valid solution

    change = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in change:
            change[coin] += 1
        else:
            change[coin] = 1
        amount -= coin

    return change


min_coins_result = find_min_coins(amount)
print(f"Optimal change for {amount}: {min_coins_result}")
