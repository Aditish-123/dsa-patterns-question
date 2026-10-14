#Find the Second Largest Element
arr = [12, 35, 1, 10, 34, 8]
largest = arr[0]
second = None

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num != largest and (second is None or num > second):
        second = num
print(second)

#Find the Element Appearing Only Once
arr = [4, 2, 4, 6, 2, 8, 8]
result = 0
for num in arr:
    result = result ^ num
print(result)


#Find the Subarray with Maximum Sum
arr = [-2, 1, -3, 4, -1, 2, 1, -5]
current = arr[0]
maximum = arr[0]
for i in range(1, len(arr)):
    current = max(arr[i], current + arr[i])
    maximum = max(maximum, current)
print(maximum)


#Find the Majority Element
arr = [2, 2, 1, 1, 1, 2, 2]
candidate = None
count = 0
for num in arr:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1
count = 0
for num in arr:
    if num == candidate:
        count += 1
if count > len(arr) // 2:
    print(candidate)
else:
    print(-1)


#Find the Length of the Longest Increasing Subsequence
arr = [10, 9, 2, 5, 3, 7, 101, 18]
dp = [1] * len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))


#Find the Pivot Index
arr = [1, 7, 3, 6, 5, 6]
left_sum = 0
right_sum = sum(arr)
for i in range(len(arr)):
    right_sum -= arr[i]
    if left_sum == right_sum:
        print(i)
        break
    left_sum += arr[i]


#Find the Number of Pairs with a Given Sum
arr = [1, 5, 7, -1, 5]
target = 6
pairs = set()
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            pairs.add(tuple(sorted((arr[i], arr[j]))))
print("Count:", len(pairs))
print(pairs)


#Find the Smallest Missing Positive Integer
arr = [3, 4, -1, 1]
num = 1
while num in arr:
    num += 1
print(num)


#Find the Maximum Product Subarray
arr = [2, 3, -2, 4]
current_max = arr[0]
current_min = arr[0]
maximum = arr[0]
for i in range(1, len(arr)):
    num = arr[i]
    if num < 0:
        current_max, current_min = current_min, current_max
    current_max = max(num, current_max * num)
    current_min = min(num, current_min * num)
    maximum = max(maximum, current_max)
print(maximum)


#Find the First Non-Repeating Character
s = "swiss"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break


#Find the Longest Palindromic Substring
s = "babad"
longest = ""
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if sub == sub[::-1]:
            if len(sub) > len(longest):
                longest = sub
print(longest)


#Find the Missing Ranges
nums = [0, 1, 3, 50, 75]
start = 0
end = 99
result = []
previous = start - 1
for num in nums + [end + 1]:
    if num - previous > 1:
        result.append([previous + 1, num - 1])
    previous = num
print(result)


#Find the Kth Smallest Element
arr = [7, 10, 4, 3, 20, 15]
k = 3
for i in range(k):
    smallest = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[smallest]:
            smallest = j
    arr[i], arr[smallest] = arr[smallest], arr[i]
print(arr[k - 1])


#Find the Longest Common Prefix
strs = ["flower", "flow", "flight"]
prefix = strs[0]
for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
print(prefix)


#Count Elements Less Than or Equal to Target
arr = [1, 2, 2, 3, 4, 5]
target = 2
low = 0
high = len(arr) - 1
answer = 0
while low <= high:
    mid = (low + high) // 2
    if arr[mid] <= target:
        answer = mid + 1
        low = mid + 1
    else:
        high = mid - 1
print(answer)