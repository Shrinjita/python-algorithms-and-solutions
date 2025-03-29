import heapq
import sys

MOD = 10**9 + 7

def lexicopolis(n, m, s, t, x, k, roads):
    # Graph representation
    graph = [[] for _ in range(n + 1)]
    for u, v, w in roads:
        graph[u].append((v, w))
    
    # DP table initialization
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[s][0] = 0
    
    # Priority Queue for lexicographical order
    pq = [(0, s, 0)]  # (path weight, current node, length of path)
    
    while pq:
        current_weight, u, length = heapq.heappop(pq)

        if length == k:
            continue

        for v, weight in graph[u]:
            new_weight = current_weight * x + weight
            if new_weight < dp[v][length + 1]:
                dp[v][length + 1] = new_weight
                heapq.heappush(pq, (new_weight, v, length + 1))
    
    # Check if there's a valid path of length k
    if dp[t][k] == float('inf'):
        return -1

    # Reconstruct the path
    result = 0
    weight = dp[t][k]
    for _ in range(k):
        result = (result * x + weight % x) % MOD
        weight //= x
    
    return result

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # Parsing input
    n, m, s, t, x, k = map(int, data[0].split())
    roads = [tuple(map(int, line.split())) for line in data[1:]]
    
    # Function call and output
    result = lexicopolis(n, m, s, t, x, k, roads)
    print(result)

if __name__ == "__main__":
    main()
