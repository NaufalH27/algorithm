testCase2 = [2, 3, 20, 4, 6, 20, 10, 4, 693, 31, 4]

def greedy_coin_change(coins : list , target : int) -> list:
    coins.sort(reverse=True)
    
    results = []
    for coin in coins:
        maxCoin = target // coin
        if(maxCoin != 0):
            results.extend([coin] * maxCoin)
            target -= coin * maxCoin
            
    return results

print(greedy_coin_change(testCase2,400))