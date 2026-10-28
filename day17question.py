#Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

#Linked List Cycle
def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

#First Bad Version
def firstBadVersion(n, bad):
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if mid >= bad:
            right = mid
        else:
            left = mid + 1
    return left
n = 5
bad = 4
print(firstBadVersion(n, bad))

#Daily Temperatures
def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    return answer
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

#Binary Tree Level Order Traversal
from collections import deque
def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

#Invert Binary Tree
def invertTree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

#Climbing Stairs
def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for i in range(3, n + 1):
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
    rows = len(image)
    cols = len(image[0])
    def dfs(r, c):
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            image[r][c] != original):
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    dfs(sr, sc)
    return image
image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
print(floodFill(image, 1, 1, 2))

#Kth Largest Element in an Array
import heapq
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
