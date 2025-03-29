def count_inversions(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    inv_a = count_inversions(a)
    inv_b = count_inversions(b)
    if inv_a == inv_b:
        print("Yes")
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))
        return
    from itertools import permutations
   
    for perm in permutations(a):
        if count_inversions(perm) == inv_b:
            print("Yes")
            print(" ".join(map(str, perm)))
            print(" ".join(map(str, b)))
            return
    print("No")
if __name__ == "__main__":
    solve()