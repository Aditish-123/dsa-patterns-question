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


#Median of Two Sorted Arrays
nums1 = [1, 3]
nums2 = [2]
arr = sorted(nums1 + nums2)
n = len(arr)
if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
print(float(median))


#Minimum Window Substring
from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"
need = Counter(t)
left = 0
start = 0
min_length = float("inf")
missing = len(t)
for right in range(len(s)):
    if need[s[right]] > 0:
        missing -= 1
    need[s[right]] -= 1
    while missing == 0:
        if right - left + 1 < min_length:
            min_length = right - left + 1
            start = left
        need[s[left]] += 1
        if need[s[left]] > 0:
            missing += 1
        left += 1
if min_length == float("inf"):
    print("")
else:
    print(s[start:start + min_length])


#Subarray Sum Equals K
arr = [1, 1, 1, 1, 1]
k = 3
count = 0
prefix_sum = 0
freq = {0: 1}
for num in arr:
    prefix_sum += num
    count += freq.get(prefix_sum - k, 0)
    freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
print(count)


#Trapping Rain Water
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
left = 0
right = len(height) - 1
left_max = 0
right_max = 0
water = 0
while left < right:
    if height[left] < height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]
        left += 1
    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]
        right -= 1
print(water)


#Group Anagrams
from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
for word in strs:
    key = "".join(sorted(word))
    groups[key].append(word)
print(list(groups.values()))


#Validate Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isValidBST(root):
    def check(node, low, high):
        if node is None:
            return True
        if not low < node.val < high:
            return False
        return (check(node.left, low, node.val) and
                check(node.right, node.val, high))
    return check(root, float("-inf"), float("inf"))
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(isValidBST(root))


#Merge Intervals
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort()
result = []
for interval in intervals:
    if not result or interval[0] > result[-1][1]:
        result.append(interval)
    else:
        result[-1][1] = max(result[-1][1], interval[1])
print(result)


#Design a Stack with Increment Operation
class CustomStack:
    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize
    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1
    def increment(self, k, val):
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
stack = CustomStack(3)
stack.push(1)
stack.push(2)
stack.increment(2, 10)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())


#Find the Duplicate Number
nums = [1, 3, 4, 2, 2]
slow = nums[0]
fast = nums[0]
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break
slow = nums[0]
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
print(slow)