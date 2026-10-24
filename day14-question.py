#N-Queens II
def totalNQueens(n):
    count = 0

    def backtrack(row, cols, diag1, diag2):
        nonlocal count

        if row == n:
            count += 1
            return

        for col in range(n):
            d1 = row - col
            d2 = row + col

            if col not in cols and d1 not in diag1 and d2 not in diag2:
                backtrack(
                    row + 1,
                    cols | {col},
                    diag1 | {d1},
                    diag2 | {d2}
                )

    backtrack(0, set(), set(), set())
    return count

print(totalNQueens(8))

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
                    result.append(word + (" " + rest if rest else ""))

        memo[start] = result
        return result

    return solve(0)


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

print(wordBreak(s, wordDict))


#Generate Parentheses
def generateParenthesis(n):
    result = []

    def backtrack(current, opened, closed):
        if len(current) == 2 * n:
            result.append(current)
            return

        if opened < n:
            backtrack(current + "(", opened + 1, closed)

        if closed < opened:
            backtrack(current + ")", opened, closed + 1)

    backtrack("", 0, 0)
    return result

print(generateParenthesis(3))

#Palindrome Partitioning II
def minCut(s):
    n = len(s)
    dp = list(range(n))

    for end in range(n):
        for start in range(end + 1):
            if s[start] == s[end] and (
                end - start <= 2 or dp[start + 1] == dp[start + 1]
            ):
                part = s[start:end + 1]

                if part == part[::-1]:
                    dp[end] = min(
                        dp[end],
                        0 if start == 0 else dp[start - 1] + 1
                    )

    return dp[-1]


print(minCut("aab"))


#Combination Sum III
def combinationSum3(k, n):
    result = []

    def backtrack(start, path, total):
        if len(path) == k:
            if total == n:
                result.append(path[:])
            return

        for num in range(start, 10):
            if total + num > n:
                break

            path.append(num)
            backtrack(num + 1, path, total + num)
            path.pop()

    backtrack(1, [], 0)
    return result


print(combinationSum3(3, 7))

#Permutations II
def permuteUnique(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(nums[i])

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    return result


print(permuteUnique([1, 1, 2]))

#Restore IP Addresses
def restoreIpAddresses(s):
    result = []

    def backtrack(start, parts):
        if len(parts) == 4:
            if start == len(s):
                result.append(".".join(parts))
            return

        for length in range(1, 4):
            part = s[start:start + length]

            if len(part) != length:
                continue

            if length > 1 and part[0] == "0":
                continue

            if int(part) > 255:
                continue

            backtrack(start + length, parts + [part])

    backtrack(0, [])
    return result


print(restoreIpAddresses("25525511135"))


#Number of Islands II
def numIslands2(m, n, positions):
    parent = {}
    rank = {}
    count = 0
    result = []

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)

        if ra == rb:
            return False

        if rank[ra] < rank[rb]:
            ra, rb = rb, ra

        parent[rb] = ra

        if rank[ra] == rank[rb]:
            rank[ra] += 1

        return True

    for r, c in positions:
        cell = (r, c)

        if cell in parent:
            result.append(count)
            continue

        parent[cell] = cell
        rank[cell] = 0
        count += 1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if 0 <= nr < m and 0 <= nc < n and neighbor in parent:
                if union(cell, neighbor):
                    count -= 1

        result.append(count)

    return result


positions = [[0, 0], [0, 1], [1, 2], [2, 1], [1, 1]]
print(numIslands2(3, 3, positions))


#Target Sum
def findTargetSumWays(nums, target):
    dp = {0: 1}

    for num in nums:
        new_dp = {}

        for total, ways in dp.items():
            plus = total + num
            minus = total - num

            new_dp[plus] = new_dp.get(plus, 0) + ways
            new_dp[minus] = new_dp.get(minus, 0) + ways

        dp = new_dp

    return dp.get(target, 0)


print(findTargetSumWays([1, 1, 1, 1, 1], 3))

#Kth Permutation Sequence
import math

def getPermutation(n, k):
    nums = list(range(1, n + 1))
    k -= 1
    result = ""

    while nums:
        fact = math.factorial(len(nums) - 1)
        index = k // fact

        result += str(nums.pop(index))
        k %= fact

    return result


print(getPermutation(4, 9))


#Path with Maximum Gold
def getMaximumGold(grid):
    rows = len(grid)
    cols = len(grid[0])
    best = 0

    def dfs(r, c, total):
        nonlocal best

        gold = grid[r][c]
        best = max(best, total + gold)
        grid[r][c] = 0

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                dfs(nr, nc, total + gold)

        grid[r][c] = gold

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                dfs(r, c, 0)

    return best


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(getMaximumGold(grid))

#Split Array into Fibonacci Sequence
def splitIntoFibonacci(num):
    result = []
    MAX = 2**31 - 1

    def backtrack(index):
        if index == len(num):
            return len(result) >= 3

        current = 0

        for i in range(index, len(num)):
            if i > index and num[index] == "0":
                break

            current = current * 10 + int(num[i])

            if current > MAX:
                break

            if len(result) >= 2:
                expected = result[-1] + result[-2]

                if current < expected:
                    continue
                if current > expected:
                    break

            result.append(current)

            if backtrack(i + 1):
                return True

            result.pop()

        return False

    return result if backtrack(0) else []


print(splitIntoFibonacci("123456579"))


#Find the Maximum Score
def maxScore(cardPoints, k):
    total = sum(cardPoints)
    window_size = len(cardPoints) - k

    if window_size == 0:
        return total

    current = sum(cardPoints[:window_size])
    min_sum = current

    for i in range(window_size, len(cardPoints)):
        current += cardPoints[i] - cardPoints[i - window_size]
        min_sum = min(min_sum, current)

    return total - min_sum


nums = [1, 2, 3, 4, 5, 6, 1]
k = 3

print(maxScore(nums, k))


#All Possible Full Binary Trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPossibleFBT(n):
    memo = {}

    def build(nodes):
        if nodes in memo:
            return memo[nodes]

        if nodes == 1:
            return [TreeNode(0)]

        result = []

        for left_count in range(1, nodes, 2):
            right_count = nodes - 1 - left_count

            for left in build(left_count):
                for right in build(right_count):
                    result.append(
                        TreeNode(0, left, right)
                    )

        memo[nodes] = result
        return result

    if n % 2 == 0:
        return []

    return build(n)


trees = allPossibleFBT(7)
print(len(trees))


#Remove Invalid Parentheses
from collections import deque

def removeInvalidParentheses(s):
    def isValid(text):
        balance = 0

        for ch in text:
            if ch == "(":
                balance += 1
            elif ch == ")":
                balance -= 1

            if balance < 0:
                return False

        return balance == 0

    queue = deque([s])
    visited = {s}

    while queue:
        level_results = []

        for _ in range(len(queue)):
            current = queue.popleft()

            if isValid(current):
                level_results.append(current)

        if level_results:
            return level_results

        for current in level_results:
            pass

        for current in list(visited):
            pass

        # Generate strings by removing one parenthesis.
        # Only process strings at the current BFS level.
        # The next level is generated below.
        break

    queue = deque([s])
    visited = {s}

    while queue:
        current = queue.popleft()
        if isValid(current):
            # BFS ensures this is a minimum-removal solution.
            result = [current]
            while queue:
                candidate = queue.popleft()
                if isValid(candidate):
                    result.append(candidate)
            return result
        for i, ch in enumerate(current):
            if ch not in "()":
                continue
            candidate = current[:i] + current[i + 1:]
            if candidate not in visited:
                visited.add(candidate)
                queue.append(candidate)
    return [""]
print(removeInvalidParentheses("()())()"))