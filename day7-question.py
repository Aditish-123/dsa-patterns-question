#Kth Largest Element in an Array
arr = [3, 2, 1, 5, 6, 4]
k = 2
arr.sort()
print(arr[-k])


#Find a Pair with the Given Difference
arr = [1, 5, 8, 12, 15]
target = 7
arr.sort()
i = 0
j = 1
while j < len(arr):
    diff = arr[j] - arr[i]
    if diff == target:
        print([arr[i], arr[j]])
        break
    elif diff < target:
        j += 1
    else:
        i += 1
    if i == j:
        j += 1
else:
    print(-1)


#Search in a 2D Matrix
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 16
found = False
for row in matrix:
    low = 0
    high = len(row) - 1
    while low <= high:
        mid = (low + high) // 2
        if row[mid] == target:
            found = True
            break
        elif row[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if found:
        break
print(found)


#Longest Consecutive Sequence
arr = [100, 4, 200, 1, 3, 2]
nums = set(arr)
longest = 0
for num in nums:
    if num - 1 not in nums:
        count = 1
        current = num
        while current + 1 in nums:
            current += 1
            count += 1
        longest = max(longest, count)
print(longest)


#Count Subarrays with Sum K
arr = [1, 2, 3, -2, 5]
k = 5
prefix_sum = 0
count = 0
seen = {0: 1}
for num in arr:
    prefix_sum += num
    needed = prefix_sum - k
    if needed in seen:
        count += seen[needed]
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
print(count)