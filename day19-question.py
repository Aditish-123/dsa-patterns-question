#4Sum
def fourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result
print(fourSum([1, 0, -1, 0, -2, 2], 0))

#Top K Frequent Elements
from collections import Counter
def topKFrequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))

#Longest Repeating Character Replacement
def characterReplacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    result = 0
    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        max_freq = max(max_freq, count[char])
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result
print(characterReplacement("AABABBA", 1))

#Permutation in String
from collections import Counter
def checkInclusion(s1, s2):
    k = len(s1)
    if k > len(s2):
        return False
    target = Counter(s1)
    window = Counter(s2[:k])
    if window == target:
        return True
    for i in range(k, len(s2)):
        window[s2[i]] += 1
        old = s2[i - k]
        window[old] -= 1
        if window[old] == 0:
            del window[old]
        if window == target:
            return True
    return False
print(checkInclusion("ab", "eidbaooo"))

#Partition Labels
def partitionLabels(s):
    last = {char: i for i, char in enumerate(s)}
    result = []
    start = 0
    end = 0
    for i, char in enumerate(s):
        end = max(end, last[char])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result
print(partitionLabels("ababcbacadefegdehijhklij"))

#Asteroid Collision
def asteroidCollision(asteroids):
    stack = []
    for asteroid in asteroids:
        alive = True
        while stack and stack[-1] > 0 and asteroid < 0:
            if stack[-1] < -asteroid:
                stack.pop()
            elif stack[-1] == -asteroid:
                stack.pop()
                alive = False
                break
            else:
                alive = False
                break
        if alive:
            stack.append(asteroid)
    return stack
print(asteroidCollision([5, 10, -5]))

#Car Fleet
def carFleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)
    fleets = 0
    last_time = 0
    for pos, spd in cars:
        time = (target - pos) / spd
        if time > last_time:
            fleets += 1
            last_time = time
    return fleets
print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))

#Task Scheduler
from collections import Counter
def leastInterval(tasks, n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = sum(1 for x in freq.values() if x == max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))

#Gas Station
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    total = 0
    start = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            start = i + 1
            total = 0
    return start
print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))

#Binary Tree Right Side View
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def rightSideView(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(rightSideView(root))

#Lowest Common Ancestor of a Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
p = root.left
q = root.right
answer = lowestCommonAncestor(root, p, q)
print(answer.val)

#Balanced Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isBalanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return height(root) != -1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(isBalanced(root))

#Clone Graph
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []
def cloneGraph(node):
    if not node:
        return None
    copies = {}
    def dfs(current):
        if current in copies:
            return copies[current]
        clone = Node(current.val)
        copies[current] = clone
        for neighbor in current.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone
    return dfs(node)

# Create a small graph
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node1]
node3.neighbors = [node1]
copied = cloneGraph(node1)
print(copied.val)
print([n.val for n in copied.neighbors])

#Pacific Atlantic Water Flow
def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()
    def dfs(r, c, visited):
        visited.add((r, c))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, visited)
    for r in range(rows):
        dfs(r, 0, pacific)
        dfs(r, cols - 1, atlantic)
    for c in range(cols):
        dfs(0, c, pacific)
        dfs(rows - 1, c, atlantic)

    return sorted([list(cell) for cell in pacific & atlantic])
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
print(pacificAtlantic(heights))

#Network Delay Time
import heapq
from collections import defaultdict
def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    distances = {k: 0}
    heap = [(0, k)]
    while heap:
        time, node = heapq.heappop(heap)
        if time > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_time = time + weight
            if new_time < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))
    if len(distances) != n:
        return -1
    return max(distances.values())
print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

#Coin Change
def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != float("inf") else -1
print(coinChange([1, 2, 5], 11))

#Edit Distance
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )
    return dp[m][n]
print(minDistance("horse", "ros"))

#Longest Common Subsequence
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )
    return dp[m][n]
print(longestCommonSubsequence("abcde", "ace"))

#Minimum Path Sum
def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]
    for r in range(1, rows):
        dp[r][0] = dp[r - 1][0] + grid[r][0]
    for c in range(1, cols):
        dp[0][c] = dp[0][c - 1] + grid[0][c]
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = grid[r][c] + min(
                dp[r - 1][c],
                dp[r][c - 1]
            )
    return dp[-1][-1]
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))

#Implement Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
trie = Trie()
trie.insert("apple")
a = trie.search("apple")
b = trie.search("app")
c = trie.startsWith("app")
trie.insert("app")
d = trie.search("app")
print([None, a, b, c, None, d])