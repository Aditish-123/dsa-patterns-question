#Find an Element
arr = [10, 25, 7, 40, 15]
target = 40
for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        break


#Check Whether Element Exists
arr = [4, 8, 12, 16, 20]
target = 12
found = False
for num in arr:
    if num == target:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")


#Count Occurrences
arr = [2, 5, 2, 8, 2, 9, 5]
target = 2
count = 0
for num in arr:
    if num == target:
        count += 1
print("Count:", count)


#Find All Positions
arr = [10, 20, 10, 30, 10, 40]
target = 10
positions = []
for i in range(len(arr)):
    if arr[i] == target:
        positions.append(i)
print(positions)


#First Occurrence
arr = [5, 3, 5, 8, 5, 9]
target = 5
for i in range(len(arr)):
    if arr[i] == target:
        print("First index:", i)
        break


#Last Occurrence
arr = [5, 3, 5, 8, 5, 9]
target = 5
for i in range(len(arr) - 1, -1, -1):
    if arr[i] == target:
        print("Last index:", i)
        break


#Binary Search
arr = [3, 7, 12, 18, 25, 31, 46]
target = 31
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Element found at index", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")


#Smallest Number Greater Than Target
arr = [3, 8, 12, 17, 25, 30]
target = 15
for num in arr:
    if num > target:
        print(num)
        break


#Find the Missing Number
arr = [1, 2, 3, 5, 6, 7]
for num in range(1, 8):
    if num not in arr:
        print("Missing number:", num)
        break


#Binary Search in Descending List
arr = [50, 40, 30, 20, 10]
target = 20
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Element found at index", mid)
        break
    elif arr[mid] > target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")


#First Occurrence Using Binary Search
arr = [2, 4, 4, 4, 7, 9, 12]
target = 4
low = 0
high = len(arr) - 1
answer = -1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        answer = mid
        high = mid - 1
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print("First occurrence at index", answer)


#Find Insert Position
arr = [1, 3, 5, 7, 9]
target = 6
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print("Insert position:", low)


#Find Peak Element
arr = [1, 3, 8, 12, 9, 5, 2]
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        print("Peak element:", arr[i])
        break


#Search in a Rotated Sorted List
arr = [15, 18, 2, 3, 6, 12]
target = 3
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Element found at index", mid)
        break
    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1
else:
    print("Not Found")


#First Number Repeated Twice
arr = [4, 7, 2, 7, 4, 9, 2]
seen = []
for num in arr:
    if num in seen:
        print("First repeated number:", num)
        break
    seen.append(num)
