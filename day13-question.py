#Serialize and Deserialize Binary Tree
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Codec:
    def serialize(self, root):
        if not root:
            return "null"
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                result.append("null")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        while result and result[-1] == "null":
            result.pop()
        return ",".join(result)
    def deserialize(self, data):
        if data == "null":
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
codec = Codec()
data = codec.serialize(root)
print(data)
print(codec.serialize(codec.deserialize(data)))


#Minimum Cost to Connect Sticks
import heapq
sticks = [2, 4, 3]
heapq.heapify(sticks)
cost = 0
while len(sticks) > 1:
    a = heapq.heappop(sticks)
    b = heapq.heappop(sticks)
    total = a + b
    cost += total
    heapq.heappush(sticks, total)
print(cost)


#Kth Smallest Element in a BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def kthSmallest(root, k):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val
        current = current.right
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kthSmallest(root, 1))


#Sudoku Solver
def solveSudoku(board):
    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in "123456789":
                        valid = True
                        for i in range(9):
                            if board[r][i] == num or board[i][c] == num:
                                valid = False
                        for i in range(3):
                            for j in range(3):
                                if board[(r // 3) * 3 + i][(c // 3) * 3 + j] == num:
                                    valid = False
                        if valid:
                            board[r][c] = num
                            if backtrack():
                                return True
                            board[r][c] = "."
                    return False
        return True
    backtrack()
    return board
board = [
    list("53..7...."),
    list("6..195..."),
    list(".98....6."),
    list("8...6...3"),
    list("4..8.3..1"),
    list("7...2...6"),
    list(".6....28."),
    list("...419..5"),
    list("....8..79")
]
for row in solveSudoku(board):
    print("".join(row))


#Longest Substring with K Distinct Characters
def longestSubstring(s, k):
    left = 0
    freq = {}
    max_length = 0
    for right in range(len(s)):
        ch = s[right]
        freq[ch] = freq.get(ch, 0) + 1
        while len(freq) > k:
            left_ch = s[left]
            freq[left_ch] -= 1
            if freq[left_ch] == 0:
                del freq[left_ch]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length
s = "eceba"
k = 2
print(longestSubstring(s, k))


#Design Twitter
from collections import defaultdict
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
    def getNewsFeed(self, userId):
        import heapq
        users = self.following[userId] | {userId}
        latest = []
        for user in users:
            for time, tweetId in self.tweets[user][-10:]:
                latest.append((time, tweetId))
        latest.sort(reverse=True)
        return [tweetId for _, tweetId in latest[:10]]
    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)
twitter = Twitter()
twitter.postTweet(1, 5)
twitter.postTweet(1, 6)
twitter.follow(2, 1)
print(twitter.getNewsFeed(2))


#Alien Dictionary
from collections import defaultdict, deque
def alienOrder(words):
    graph = defaultdict(set)
    indegree = {ch: 0 for word in words for ch in word}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
        for a, b in zip(w1, w2):
            if a != b:
                if b not in graph[a]:
                    graph[a].add(b)
                    indegree[b] += 1
                break
    queue = deque([ch for ch in indegree if indegree[ch] == 0])
    result = []
    while queue:
        ch = queue.popleft()
        result.append(ch)
        for neighbor in graph[ch]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return "".join(result) if len(result) == len(indegree) else ""
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words))


#Maximum Path Sum in a Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxPathSum(root):
    best = float("-inf")
    def dfs(node):
        nonlocal best
        if not node:
            return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        best = max(best, node.val + left + right)
        return node.val + max(left, right)
    dfs(root)
    return best
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(maxPathSum(root))


#Partition Equal Subset Sum
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = {0}
    for num in nums:
        new_sums = set()
        for current in dp:
            new_sums.add(current + num)
        dp |= new_sums
        if target in dp:
            return True
    return target in dp
nums = [1, 5, 11, 5]
print(canPartition(nums))


#Course Schedule II
from collections import defaultdict, deque
def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1
    queue = deque(
        i for i in range(numCourses)
        if indegree[i] == 0
    )
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == numCourses else []
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(findOrder(numCourses, prerequisites))


#Word Break II
def wordBreak(s, wordDict):
    words = set(wordDict)
    memo = {}
    def solve(start):
        if start == len(s):
            return [""]
        if start in memo:
            return memo[start]
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in words:
                for rest in solve(end):
                    if rest:
                        result.append(word + " " + rest)
                    else:
                        result.append(word)
        memo[start] = result
        return result
    return solve(0)
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s, wordDict))


#Maximal Rectangle
def maximalRectangle(matrix):
    if not matrix:
        return 0
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0
    for row in matrix:
        for j in range(cols):
            if row[j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0
        stack = []
        for i in range(cols + 1):
            current = heights[i] if i < cols else 0
            while stack and heights[stack[-1]] > current:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
    return max_area
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(maximalRectangle(matrix))


#Reconstruct Itinerary
from collections import defaultdict
def findItinerary(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    for airport in graph:
        graph[airport].sort(reverse=True)
    route = []
    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        route.append(airport)
    dfs("JFK")
    return route[::-1]
tickets = [
    ["MUC", "LHR"],
    ["JFK", "MUC"],
    ["SFO", "SJC"],
    ["LHR", "SFO"]
]
print(findItinerary(tickets))


#Longest Palindromic Substring
def longestPalindrome(s):
    result = ""
    for i in range(len(s)):
        for left, right in [(i, i), (i, i + 1)]:
            while (left >= 0 and right < len(s)
                   and s[left] == s[right]):
                if right - left + 1 > len(result):
                    result = s[left:right + 1]
                left -= 1
                right += 1
    return result
s = "babad"
print(longestPalindrome(s))


#Find Median from Data Stream
import heapq
class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap, negative values
        self.large = []  # Min heap
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        if self.large and -self.small[0] > self.large[0]:
            heapq.heappush(
                self.large,
                -heapq.heappop(self.small)
            )
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(
                self.large,
                -heapq.heappop(self.small)
            )
        elif len(self.large) > len(self.small):
            heapq.heappush(
                self.small,
                -heapq.heappop(self.large)
            )
    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())