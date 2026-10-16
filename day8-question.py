#Move Zeroes
arr = [0, 1, 0, 3, 12]
pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1
while pos < len(arr):
    arr[pos] = 0
    pos += 1
print(arr)


#Remove Duplicates from Sorted Array II
arr = [1, 1, 1, 2, 2, 3]
k = 0
for num in arr:
    if k < 2 or num != arr[k - 2]:
        arr[k] = num
        k += 1
print("Length:", k)
print("Array:", arr[:k])


#Container With Most Water
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
left = 0
right = len(height) - 1
maximum = 0
while left < right:
    width = right - left
    h = min(height[left], height[right])
    area = width * h
    maximum = max(maximum, area)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
print(maximum)


#Find the Duplicate Number
arr = [1, 3, 4, 2, 2]
slow = arr[0]
fast = arr[0]
while True:
    slow = arr[slow]
    fast = arr[arr[fast]]
    if slow == fast:
        break
slow = arr[0]
while slow != fast:
    slow = arr[slow]
    fast = arr[fast]

print(slow)
