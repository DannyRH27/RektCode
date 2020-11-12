def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    # Write your code here!

    coins = []
    stack = list(coins_available)
    while v > 0:
        coin = stack.pop()
        num_coins = v // coin
        v -= (num_coins * coin)
        while num_coins > 0:
            coins.append(coin)
            num_coins -= 1

    return coins
