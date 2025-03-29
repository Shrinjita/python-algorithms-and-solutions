def rod_cutting(prices, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, prices[j] + dp[i - j - 1])
        dp[i] = max_val
    return dp[n]
def main():
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    n = int(input("Enter the length of the rod: "))
    max_profit = rod_cutting(prices, n)
    print(max_profit)
if __name__ == "__main__":
    main()
