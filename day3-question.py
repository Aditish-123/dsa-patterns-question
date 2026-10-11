#Snake Number Matrix (5 × 5)
n = 5
num = 1
for i in range(n):
    row = []

    for j in range(n):
        row.append(num)
        num += 1
    if i % 2 == 1:
        row.reverse()
    print(*row)

#Alphabet Rangoli (n = 4)
n = 4
for i in range(n):
    letters = []
    for j in range(i + 1):
        letters.append(chr(96 + n - j))
    left = letters[::-1]
    right = letters[1:]
    row = left + right
    print("-".join(row).center(13, "-"))
for i in range(n - 2, -1, -1):
    letters = []
    for j in range(i + 1):
        letters.append(chr(96 + n - j))
    row = letters[::-1] + letters[1:]
    print("-".join(row).center(13, "-"))

#Diagonal Zigzag Matrix (4 × 4)
n = 4
matrix = [[0] * n for _ in range(n)]
num = 1
for diagonal in range(2 * n - 1):
    cells = []
    for i in range(n):
        j = diagonal - i
        if 0 <= j < n:
            cells.append((i, j))
    if diagonal % 2 == 0:
        cells.reverse()
    for i, j in cells:
        matrix[i][j] = num
        num += 1
for row in matrix:
    print(*row)


#Bubble sort 
arr = [5, 2, 4, 1, 3]
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

#Quick sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left) + [pivot] + quick_sort(right)
arr = [5, 2, 4, 1, 3]
print(quick_sort(arr))

#Merge sort 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result
arr = [5, 2, 4, 1, 3]
print(merge_sort(arr))

