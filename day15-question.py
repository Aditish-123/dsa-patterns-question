#Split Array Largest Sum
def splitArray(nums, k):
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        subarrays = 1
        current_sum = 0
        for num in nums:
            if current_sum + num > mid:
                subarrays += 1
                current_sum = num
            else:
                current_sum += num
        if subarrays <= k:
            right = mid
        else:
            left = mid + 1
    return left
nums = [7, 2, 5, 10, 8]
k = 2
print(splitArray(nums, k))

#Sum of Subarray Minimums
def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    stack = []
    result = 0
    for i in range(len(arr) + 1):
        current = arr[i] if i < len(arr) else 0
        while stack and arr[stack[-1]] > current:
            index = stack.pop()
            left = stack[-1] if stack else -1
            right = i
            count = (index - left) * (right - index)
            result += arr[index] * count
        stack.append(i)
    return result % MOD
arr = [3, 1, 2, 4]
print(sumSubarrayMins(arr))

#Burst Balloons
def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for last in range(left + 1, right):
                coins = (
                    nums[left] * nums[last] * nums[right]
                    + dp[left][last]
                    + dp[last][right]
                )
                dp[left][right] = max(
                    dp[left][right], coins
                )
    return dp[0][n - 1]
nums = [3, 1, 5, 8]
print(maxCoins(nums))

#Insert Delete GetRandom O(1)
import random
class RandomizedSet:
    def __init__(self):
        self.values = []
        self.positions = {}
    def insert(self, val):
        if val in self.positions:
            return False
        self.positions[val] = len(self.values)
        self.values.append(val)
        return True
    def remove(self, val):
        if val not in self.positions:
            return False
        index = self.positions[val]
        last = self.values[-1]
        self.values[index] = last
        self.positions[last] = index
        self.values.pop()
        del self.positions[val]
        return True
    def getRandom(self):
        return random.choice(self.values)
obj = RandomizedSet()
print(obj.insert(10))
print(obj.insert(20))
print(obj.insert(10))
print(obj.remove(10))
print(obj.getRandom())

#IPO — Maximize Capital
import heapq
def findMaximizedCapital(k, w, profits, capital):
    projects = sorted(zip(capital, profits))
    max_heap = []
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1])
            i += 1
        if not max_heap:
            break
        w += -heapq.heappop(max_heap)
    return w
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(findMaximizedCapital(k, w, profits, capital))