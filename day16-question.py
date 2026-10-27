#Contains Duplicate
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
print(containsDuplicate([1, 2, 3, 1]))

#Move Zeroes
def moveZeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    while index < len(nums):
        nums[index] = 0
        index += 1
    return nums
print(moveZeroes([0, 1, 0, 3, 12]))

#Best Time to Buy and Sell Stock
def maxProfit(prices):
    min_price = prices[0]
    profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit
print(maxProfit([7, 1, 5, 3, 6, 4]))

#Valid Anagram
def isAnagram(s, t):
    return sorted(s) == sorted(t)
print(isAnagram("listen", "silent"))

#Missing Number
def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
print(missingNumber([3, 0, 1]))

#Majority Element
def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))

#Longest Common Prefix
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix
print(longestCommonPrefix(["flower", "flow", "flight"]))

#Search in Rotated Sorted Array
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
print(search([4, 5, 6, 7, 0, 1, 2], 0))

#implement Queue Using Stacks
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x):
        self.stack1.append(x)
    def transfer(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
    def pop(self):
        self.transfer()
        return self.stack2.pop()
    def peek(self):
        self.transfer()
        return self.stack2[-1]
    def empty(self):
        return not self.stack1 and not self.stack2
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(q.empty())

#Number of 1 Bits
def hammingWeight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
print(hammingWeight(11))