def is_valid(array, b):
    # Check if the current array matches the product constraints
    for i in range(len(b)):
        if array[i] * array[i + 1] != b[i]:
            return False
    return True

def backtrack(array, b, n):
    if len(array) == n:
        if is_valid(array, b):
            return array
        else:
            return None
    
    for i in range(1, 101):
        if i not in array:
            array.append(i)
            result = backtrack(array, b, n)
            if result:
                return result
            array.pop()
    
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    b = list(map(int, data[1:]))
    
    result = backtrack([], b, n)
    if result:
        print("Yes")
        print(" ".join(map(str, result)))
    else:
        print("No")

if __name__ == "__main__":
    main()
