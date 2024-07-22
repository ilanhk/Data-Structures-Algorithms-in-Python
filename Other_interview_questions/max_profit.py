# List: Max Profit ( ** Interview Question)
# You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day.

# You are allowed to buy one share of the stock on one day and sell it on a later day.

# Your task is to write a function called max_profit that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

# Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

# Constraints:



# Each element of the input list is a positive integer representing the stock price for a specific day.



# Function signature: def max_profit(prices):

# Example:

# Input: prices = [7, 1, 5, 3, 6, 4]
# Function call: profit = max_profit(prices)
# Output: profit = 5

# Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.


# WRITE MAX_PROFIT FUNCTION HERE #

# My solution that works:
# def max_profit(prices):
#     best_price = prices[0]
#     best_price_index = 0
#     max_profit= 0
    
#     for price in prices:
#         if price < best_price:
#             best_price = price
#             best_price_index = prices.index(price)
        
#     for i in range(best_price_index, len(prices)):
#         profit = prices[i] - best_price
#         if profit > max_profit:
#             max_profit = profit
            
#     return max_profit
  
# The course's solution
def max_profit(prices):
   
    min_price = float('inf')  # Initialize min_price to positive infinity
   
    max_profit = 0
 
    # Iterate through the list of stock prices
    for price in prices:
        
        min_price = min(min_price, price) # Update min_price with the lowest price so far
        
        profit = price - min_price # Calculate profit by selling at the current price
        
        max_profit = max(max_profit, profit) # Update max_profit with the highest profit so far
 
    # Return the maximum profit after iterating
    return max_profit
        
##################################
    
    


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""