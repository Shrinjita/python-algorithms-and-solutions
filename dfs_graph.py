from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Adds a directed edge from u to v."""
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        """Recursive utility function for DFS traversal."""
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        """Performs DFS starting from a given vertex."""
        visited = set()
        self.dfs_util(start_vertex, visited)

if __name__ == "__main__":
    g = Graph()

    edges = int(input("Enter the number of edges: ").strip())
    print("Enter edges (u v):")
    
    for _ in range(edges):
        try:
            u, v = map(int, input().strip().split())
            g.add_edge(u, v)
        except ValueError:
            print("Invalid input. Please enter two integers.")

    start_vertex = int(input("Enter the starting vertex for DFS traversal: ").strip())

    print("\nDepth First Traversal:")
    g.dfs(start_vertex)
    print()  # Print newline for better output formatting
