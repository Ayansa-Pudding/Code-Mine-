def stock(prices):
    if not prices or len(prices)<2:
        return 0
    
    total_profit=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            total_profit+=prices[i]-prices[i-1]
            
    return total_profit

prices = [635,864,400,257,745,9090909]
profit = stock(prices)
print(f"The maximum profit from multiple transactions is:{profit}")