#5  
# 2 4 8 64 16  
# 1 4  
def count_dividing_elements(arr, L, R):
    count = 0
    for num in arr:
        if all(num % i == 0 for i in range(L, R+1)):
            count += 1
    return count
N = int(input())
arr = list(map(int, input().split()))
L, R = map(int, input().split())
result = count_dividing_elements(arr, L, R)
print(result)
