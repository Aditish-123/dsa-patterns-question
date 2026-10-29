#Two Sum
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []
print(twoSum([2, 7, 11, 15], 9))

#Remove Nth Node From End of List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
def buildList(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next
def printList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
head = buildList([1, 2, 3, 4, 5])
printList(removeNthFromEnd(head, 2))

#Middle of the Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
def buildList(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def printList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
head = buildList([1, 2, 3, 4, 5, 6])
printList(middleNode(head))

#Isomorphic Strings
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    map1 = {}
    map2 = {}
    for a, b in zip(s, t):
        if a in map1 and map1[a] != b:
            return False
        if b in map2 and map2[b] != a:
            return False
        map1[a] = b
        map2[b] = a
    return True
print(isIsomorphic("egg", "add"))

#Evaluate Reverse Polish Notation
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                result = int(a / b)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[-1]
print(evalRPN(["2", "1", "+", "3", "*"]))

#Valid Parentheses
def isValid(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
print(isValid("{[()]}"))

#Merge Two Sorted Linked Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return dummy.next
def buildList(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next
def printList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
list1 = buildList([1, 2, 4])
list2 = buildList([1, 3, 4])
printList(mergeTwoLists(list1, list2))

#Find First and Last Position of Element
def searchRange(nums, target):
    def findPosition(first):
        left, right = 0, len(nums) - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                answer = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return answer
    return [findPosition(True), findPosition(False)]
print(searchRange([5, 7, 7, 8, 8, 10], 8))

#Kth Largest Element in an Array
import heapq
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))

#Find Pivot Index
def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        right_sum = total - left_sum - num
        if left_sum == right_sum:
            return i
        left_sum += num
    return -1
print(pivotIndex([1, 7, 3, 6, 5, 6]))

#Ransom Note
from collections import Counter
def canConstruct(ransomNote, magazine):
    available = Counter(magazine)
    for char in ransomNote:
        if available[char] == 0:
            return False
        available[char] -= 1
    return True
print(canConstruct("aa", "aab"))

#Climbing Stairs
def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
print(climbStairs(5))

#House Robber
def rob(nums):
    prev2 = 0
    prev1 = 0
    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current
    return prev1
print(rob([2, 7, 9, 3, 1]))

#Flood Fill
def floodFill(image, sr, sc, color):
    original = image[sr][sc]
    if original == color:
        return image
    rows, cols = len(image), len(image[0])
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or image[r][c] != original):
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    dfs(sr, sc)
    return image
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(floodFill(image, 1, 1, 2))

#Kth Largest Element in a Stream
import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)
    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
obj = KthLargest(3, [4, 5, 8, 2])
print(obj.heap[0])

#Number of Islands
def numIslands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] != "1"):
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"]
]
print(numIslands(grid))

#Rotting Oranges
from collections import deque
def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue and fresh > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid))

#Decode Ways
def numDecodings(s):
    if not s or s[0] == "0":
        return 0
    prev2 = 1
    prev1 = 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != "0":
            current += prev1
        two_digit = int(s[i - 1:i + 1])
        if 10 <= two_digit <= 26:
            current += prev2
        prev2, prev1 = prev1, current
    return prev1
print(numDecodings("226"))

#Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    longest = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        longest = max(longest, right - left + 1)
    return longest
print(lengthOfLongestSubstring("abcabcbb"))

#Word Search
def exist(board, word):
    rows, cols = len(board), len(board[0])
    def dfs(r, c, index):
        if index == len(word):
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[index]):
            return False
        original = board[r][c]
        board[r][c] = "#"
        found = (
            dfs(r + 1, c, index + 1)
            or dfs(r - 1, c, index + 1)
            or dfs(r, c + 1, index + 1)
            or dfs(r, c - 1, index + 1)
        )
        board[r][c] = original
        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
print(exist(board, "ABCCED"))