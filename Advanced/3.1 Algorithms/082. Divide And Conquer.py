import math

# -------------------------------
# 1. Merge Sort
# -------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -------------------------------
# 2. Quick Sort
# -------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# -------------------------------
# 3. Binary Search
# -------------------------------
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


# -------------------------------
# 4. Maximum Subarray (Divide & Conquer)
# -------------------------------
def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0

    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    right_sum = float('-inf')
    total = 0

    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum


def max_subarray(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    return max(
        max_subarray(arr, left, mid),
        max_subarray(arr, mid + 1, right),
        max_crossing_sum(arr, left, mid, right)
    )


# -------------------------------
# 5. Closest Pair of Points
# -------------------------------
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_pair(points):
    points.sort()

    def solve(points):
        n = len(points)

        if n <= 3:
            return min(
                distance(points[i], points[j])
                for i in range(n)
                for j in range(i + 1, n)
            )

        mid = n // 2
        mid_x = points[mid][0]

        d = min(
            solve(points[:mid]),
            solve(points[mid:])
        )

        strip = [p for p in points if abs(p[0] - mid_x) < d]
        strip.sort(key=lambda x: x[1])

        min_dist = d
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                min_dist = min(min_dist, distance(strip[i], strip[j]))

        return min_dist

    return solve(points)


# -------------------------------
# 6. Karatsuba Multiplication
# -------------------------------
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0


# -------------------------------
# 7. Strassen’s Matrix Multiplication
# -------------------------------
def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    # Combine results
    new_matrix = []
    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])
    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Merge Sort:", merge_sort(arr))
    print("Quick Sort:", quick_sort(arr))

    sorted_arr = merge_sort(arr)
    print("Binary Search (43):", binary_search(sorted_arr, 43))

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Max Subarray:", max_subarray(nums, 0, len(nums) - 1))

    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("Closest Pair Distance:", closest_pair(points))

    print("Karatsuba:", karatsuba(1234, 5678))

    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("Strassen Matrix Multiply:", strassen(A, B))
