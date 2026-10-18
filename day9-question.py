#3Sum
arr = [-1, 0, 1, 2, -1, -4]
arr.sort()

result = []

for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i - 1]:
        continue

    left = i + 1
    right = len(arr) - 1

    while left < right:
        total = arr[i] + arr[left] + arr[right]

        if total == 0:
            result.append([arr[i], arr[left], arr[right]])
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1

            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

print(result)

#Longest Subarray with Sum K
arr = [1, 2, 1, 1, 1, 3, 2]
k = 5

max_length = 0

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total += arr[j]

        if total == k:
            length = j - i + 1
            max_length = max(max_length, length)

print(max_length)

#Sort Colors
arr = [2, 0, 2, 1, 1, 0]

low = 0
mid = 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1

    elif arr[mid] == 1:
        mid += 1

    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(arr)

#Longest Substring Without Repeating Characters
s = "abcabcbb"

left = 0
seen = {}
max_length = 0
longest = ""

for right in range(len(s)):
    if s[right] in seen and seen[s[right]] >= left:
        left = seen[s[right]] + 1

    seen[s[right]] = right

    if right - left + 1 > max_length:
        max_length = right - left + 1
        longest = s[left:right + 1]

print(max_length)
print(longest)


#Product of Array Except Self
arr = [1, 2, 3, 4]
n = len(arr)

result = [1] * n

left = 1
for i in range(n):
    result[i] = left
    left *= arr[i]

right = 1
for i in range(n - 1, -1, -1):
    result[i] *= right
    right *= arr[i]

print(result)
