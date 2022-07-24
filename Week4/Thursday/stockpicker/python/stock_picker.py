def picker(prices):

    days = [0,0]
    profit = 0
    for i in range(len(prices)-1, -1, -1):
        for j in range(0, i):
            if (prices[i] - prices[j]) > profit:
                profit = prices[i] - prices[j]
                days[0] = j
                days[1] = i
    return days
    
