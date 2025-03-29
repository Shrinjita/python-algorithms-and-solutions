def calculate_final_maximum_profit(initial_profits):
    # Blue Magic: Double the profits
    blue_magic_profits = [2 * profit for profit in initial_profits]
    
    # Calculate the profit from Blue Magic
    profit_after_blue_magic = sum(blue_magic_profits)

    # Green Magic: Find the maximum additional profit by flipping the sign
    n = len(initial_profits)
    best_green_magic_profit = 0
    current_sum = 0
    max_sum = float('-inf')
    
    for i in range(n):
        # Transform the profits array into the form needed for maximum subarray sum calculation
        transformed_profit = blue_magic_profits[i] - initial_profits[i]
        current_sum = max(transformed_profit, current_sum + transformed_profit)
        max_sum = max(max_sum, current_sum)
    
    best_green_magic_profit = max_sum
    
    # Final maximum profit
    final_maximum_profit = profit_after_blue_magic + best_green_magic_profit
    return final_maximum_profit

# Test Case 1
initial_profits1 = [-2, 5, -3, 4, -1]
print("Final Maximum Profit (Test Case 1):", calculate_final_maximum_profit(initial_profits1))

# Test Case 2
initial_profits2 = [-1, -1, -1, -1, -1, -1, -1]
print("Final Maximum Profit (Test Case 2):", calculate_final_maximum_profit(initial_profits2))

# Test Case 3
initial_profits3 = [998244353, 864197532, -7, 1000000000]
print("Final Maximum Profit (Test Case 3):", calculate_final_maximum_profit(initial_profits3))
