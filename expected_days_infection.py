MOD = 10**9 + 7

def mod_inverse(a, mod):
    # Calculate multiplicative inverse of a under modulo using Fermat's little theorem
    return pow(a, mod - 2, mod)

def calculate_expected_days(n, m, d0, d1, d2, seating):
    total_days_if_all_infected = 0
    total_days_if_all_not_infected = 0
    uncertain_count = 0

    # Calculate the total days for both scenarios
    for i in range(n):
        for j in range(m):
            if seating[i][j] == 'V':
                total_days_if_all_infected += d0  # Infected
                total_days_if_all_not_infected += d0  # Infected
            elif seating[i][j] == '.':
                total_days_if_all_infected += d2  # Not infected
                total_days_if_all_not_infected += d2  # Not infected
            elif seating[i][j] == '?':
                total_days_if_all_infected += d0  # Treat as infected
                total_days_if_all_not_infected += d2  # Treat as not infected
                uncertain_count += 1
    
    # Modulo 10^9 + 7 for both totals
    total_days_if_all_infected %= MOD
    total_days_if_all_not_infected %= MOD

    # Calculate the expected days as (days_infected + days_not_infected) / 2^uncertain_count
    p = (total_days_if_all_infected + total_days_if_all_not_infected) % MOD
    q = pow(2, uncertain_count, MOD)

    # Calculate multiplicative inverse of q under MOD
    q_inverse = mod_inverse(q, MOD)

    # Calculate the result
    result = (p * q_inverse) % MOD

    return result

# Read input
n, m, d0, d1, d2 = map(int, input().split())
seating = [input().strip() for _ in range(n)]

# Get the expected total number of days
result = calculate_expected_days(n, m, d0, d1, d2, seating)

# Print the result
print(result)
