def find_true_false_position(n):
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2

        # Read the value at mid
        print(f"READ {mid}", flush=True)
        mid_val = input().strip()  # Expecting "true" or "false"

        # Read the value at mid + 1
        print(f"READ {mid + 1}", flush=True)
        next_val = input().strip()  # Expecting "true" or "false"

        # If we found true followed by false, return the position
        if mid_val == "true" and next_val == "false":
            print(f"OUTPUT {mid}", flush=True)
            return

        # If mid_val is "true", the answer is to the right (we need false)
        if mid_val == "true":
            left = mid + 1
        else:
            right = mid - 1

def main():
    # Reading number of test cases
    t = int(input())
    
    for _ in range(t):
        # Input length of the array for this test case
        n = int(input())
        # Find the required position interactively
        find_true_false_position(n)

# Run the main function
if __name__ == "__main__":
    main()
