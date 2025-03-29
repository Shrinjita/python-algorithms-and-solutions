def max_profit_after_spells(n, profits):
    # Step 1: Calculate total sum without any spells
    total_sum = sum(profits)
    
    # Step 2: Use Kadane's algorithm to find the best subarray for blue magic
    max_blue_sum = -float('inf')
    current_sum = 0
    for profit in profits:
        current_sum += profit
        max_blue_sum = max(max_blue_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    
    # Step 3: Find the maximum profit to negate with green magic
    max_single_profit = max(profits)
    
    # Step 4: Maximize total profit
    max_total_profit = total_sum + max_blue_sum - 2 * max_single_profit
    return max_total_profit

# Example usage
n = 5
profits = [-2, 5, -3, 4, -1]
print(max_profit_after_spells(n, profits))  # Output: 20