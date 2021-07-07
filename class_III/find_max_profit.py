# Returns the max profit that can be made with a single buy
# and sell
# You have to buy before selling (no shorting allowed)

# bitcoing_prices = [1050, 270, 1540, 3800, 2]
# find_max_profit(bitcoin_prices) -> should return 3530, which 
# is the max profit you can make from these prices by buying
# at 270 and selling at 3800

# Why 3800 and 270?
# If we want the max profit, take the largest price and the 
# smallest price and subtract
# Whatever price we buy at, we can only subtract that from
# prices that appear to the left of the buying price in
# order to get our profit

# 1. Run through multiple examples, including ones you come
#    up with yourself
# 2. Ask questions as a way to inform a checklist of tasks
#    that need to be handled

# bitcoin_prices = [10, 7, 5, 8, 11, 9]
# max profit we can make here is buying at 5, and
# selling at 11 -> 6

# bitcoin_prices = [100, 90, 80, 50, 20, 10]
# since the price keeps dropping all day, we can't
# make a profit -> 0

# Boils down to: find the max difference between two prices
# where the first price is what we buy at and the second
# price is what we sell at, taking into account that second
# price needs to come after the first price in the array

def find_max_profit(prices):
    # find the largest differences in the values and toss out
    # any differences that result from shorting (selling
    # # before buying) - idea

    # if first index is the largest value in the entire array,
    # then profit is 0 - idea

    # keep a current_max
    current_max = 0

    # loop through all the prices
    while __ :
        for i in range(len(prices)):
            # for each price, subtract every price that comes
            # before this price from the current price and
            # see if that results in a larger current_max
            if prices[i-1]:
                diff = prices[i] - prices[i-1]
                if diff > current_max:
                    print(current_max)
                    current_max = diff
                    
    return current_max

if __name__ == "__main__":
    bitcoin_prices = [10, 7, 5, 8, 11, 9]

    print(find_max_profit(bitcoin_prices)) #> 6

    # breakpoint()