def change(money):
    """
    input: an integer money
    output: minimum number of coins needed to change the given value into coins with denominations 1, 5 and 10
    """
    totalCoins = 0 
    coins = [10, 5, 1]
    
    for coin in coins: 
        coins_used = money // coin
        totalCoins += coins_used

        money -= coins_used*coin

        if money == 0: 
            break

    return totalCoins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
