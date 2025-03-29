def min_rearrangement_time(n, m, d, x, slabs):
    # Sort slabs by leftmost position
    slabs.sort()

    # List to store valid gaps for the new slab
    possible_positions = []
    
    # Check gap before the first slab
    if slabs[0][0] >= x:
        possible_positions.append((0, slabs[0][0] - x))

    # Check gaps between slabs
    for i in range(n - 1):
        left_gap = slabs[i][1] + d
        right_gap = slabs[i + 1][0] - d
        if right_gap - left_gap >= x:
            possible_positions.append((left_gap, right_gap - x))

    # Check gap after the last slab
    if m - slabs[-1][1] >= x:
        possible_positions.append((slabs[-1][1] + d, m - x))

    # Find minimum rearrangement time
    min_time = float('inf')

    for start, end in possible_positions:
        current_time = 0
        for li, ri in slabs:
            if ri < start or li > end:
                continue  # Skip unaffected slabs
            if li < start:
                current_time += start - li
            if ri > end:
                current_time += ri - end
        
        min_time = min(min_time, current_time)
    
    return min_time if min_time != float('inf') else -1

def main():
    # Read input
    n, m, d, x = map(int, input().split())
    slabs = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Compute and print the minimum rearrangement time
    print(min_rearrangement_time(n, m, d, x, slabs))

if __name__ == "__main__":
    main()
