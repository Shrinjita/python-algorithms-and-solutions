import heapq
from collections import defaultdict, deque

def find_order_of_projects(n, m, prerequisites):
    adj_list = defaultdict(list)
    indegree = [0] * (n + 1)
    for a, b in prerequisites:
        adj_list[a].append(b)
        indegree[b] += 1
    min_heap = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(min_heap, i)

    order = []
    while min_heap:
        current = heapq.heappop(min_heap)
        order.append(current)

        for neighbor in adj_list[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(min_heap, neighbor)
    if len(order) == n:
        return order
    else:
        return "IMPOSSIBLE"
def main():
    n, m = map(int, input().split())
    prerequisites = [tuple(map(int, input().split())) for _ in range(m)]
    
    result = find_order_of_projects(n, m, prerequisites)
    
    if result == "IMPOSSIBLE":
        print(result)
    else:
        print(" ".join(map(str, result)))
if __name__ == "__main__":
    main()
