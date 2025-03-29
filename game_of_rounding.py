def game_of_rounding(t, cases):
    results = []
    
    for case in cases:
        n = case[0]
        points = case[1]
        
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + points[i]
        
        result = []
        for l in range(n):
            max_score = -1
            min_levels = n
            
            for r in range(l, n):
                total_points = prefix_sums[r + 1] - prefix_sums[l]
                num_levels = r - l + 1
                avg = total_points / num_levels
                rounded_score = round(avg)
                
                if rounded_score > max_score:
                    max_score = rounded_score
                    min_levels = num_levels
                elif rounded_score == max_score:
                    min_levels = min(min_levels, num_levels)
            
            result.append(min_levels)
        
        results.append(" ".join(map(str, result)))
    
    return "\n".join(results)

# Reading input
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    cases = []
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        points = list(map(int, data[index + 1].split()))
        cases.append((n, points))
        index += 2
    
    output = game_of_rounding(t, cases)
    print(output)
