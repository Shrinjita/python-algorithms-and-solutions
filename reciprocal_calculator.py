def reciprocal(x):
    try:
        num = float(x)

        # Handle the case where num is zero
        if num == 0.0:
            return 'inf'

        # Return the reciprocal with precision of 10^-6
        return format(1.0 / num, '.6f')

    except ValueError:
        # Handle special cases for 'inf', '-inf', and 'nan'
        if x.lower() == 'inf':
            return '0'
        elif x.lower() == '-inf':
            return '0'
        elif x.lower() == 'nan':
            return 'NaN'
        else:
            return 'Invalid input'

# Read the number of inputs
n = int(input())

# Process each floating point input
for _ in range(n):
    number = input().strip()
    print(reciprocal(number))
