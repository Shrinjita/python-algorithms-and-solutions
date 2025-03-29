#HILL CLIMBING
import random

def generate_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        neighbor = state[:]  # Create a copy of the current state
        # Generate a neighboring state by incrementing or decrementing one element
        neighbor[i] += random.choice([-1, 1])
        neighbors.append(neighbor)
    return neighbors

def hill_climbing(f, x0):
    x = x0
    while True:
        neighbors = generate_neighbors(x)
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x):
            return x
        x = best_neighbor

# Example usage:
# Define an objective function
def objective_function(x):
    return sum(x)

# Initial state
current_state = [3, 5, 2]
print("Current state:", current_state)

# Perform hill climbing
final_state = hill_climbing(objective_function, current_state)
print("Final state:", final_state)
print("Objective function value of final state:", objective_function(final_state))
