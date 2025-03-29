#KNAPSACK
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

if __name__ == '__main__':
    n = int(input("Enter the number of items: "))
    weight = list(map(int, input("Enter the weights of the items: ").split()))
    profit = list(map(int, input("Enter the profits of the items: ").split()))
    W = int(input("Enter the maximum capacity of the knapsack: "))

    print("Maximum profit:", knapSack(W, weight, profit, n))
