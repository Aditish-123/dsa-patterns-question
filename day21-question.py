#Minimum Swaps to Sort an Array
def min_swaps(arr):
    n = len(arr)
    pairs = sorted((value, i) for i, value in enumerate(arr))
    visited = [False] * n
    swaps = 0
    for i in range(n):
        if visited[i] or pairs[i][1] == i:
            continue
        cycle = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = pairs[j][1]
            cycle += 1
        swaps += cycle - 1
    return swaps
arr = [4, 3, 2, 1]
print(min_swaps(arr))

#Minimum Swaps to Group Elements Together
def min_swaps(arr, k):
    good = sum(1 for x in arr if x <= k)
    if good == 0:
        return 0
    bad = sum(1 for x in arr[:good] if x > k)
    answer = bad
    for i in range(good, len(arr)):
        if arr[i - good] > k:
            bad -= 1
        if arr[i] > k:
            bad += 1
        answer = min(answer, bad)
    return answer
arr = [2, 1, 5, 6, 3, 8, 4]
print(min_swaps(arr, 3))

#Job Sequencing with Deadlines
def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)
    max_deadline = max(job[0] for job in jobs)
    slots = [False] * (max_deadline + 1)
    count = 0
    profit = 0
    for deadline, value in jobs:
        for j in range(deadline, 0, -1):
            if not slots[j]:
                slots[j] = True
                count += 1
                profit += value
                break
    return count, profit
jobs = [(4, 20), (1, 10), (1, 40), (1, 30)]
print(job_sequencing(jobs))

#Allocate Minimum Number of Pages
def can_allocate(arr, students, limit):
    count = 1
    pages = 0
    for x in arr:
        if pages + x > limit:
            count += 1
            pages = x
        else:
            pages += x
    return count <= students
def allocate_pages(arr, students):
    if students > len(arr):
        return -1
    low = max(arr)
    high = sum(arr)
    answer = high
    while low <= high:
        mid = (low + high) // 2
        if can_allocate(arr, students, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer
print(allocate_pages([12, 34, 67, 90], 2))

#Stock Buy and Sell – At Most Two Transactions
def max_profit(prices):
    buy1 = float('-inf')
    sell1 = 0
    buy2 = float('-inf')
    sell2 = 0
    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    return sell2
print(max_profit([3, 3, 5, 0, 0, 3]))

#Longest Palindromic Subsequence
def longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i + 1][j],
                    dp[i][j - 1]
                )
    return dp[0][n - 1]
print(longest_palindrome("bbbab"))

#Interleaving String
def is_interleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [[False] * (len(s2) + 1)
          for _ in range(len(s1) + 1)]
    dp[0][0] = True
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] |= dp[i - 1][j]
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] |= dp[i][j - 1]
    return dp[-1][-1]
print(is_interleave("aabcc", "dbbca", "aadbbcbcac"))

#0/1 Knapsack Problem
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )
    return dp[capacity]
weights = [10, 20, 30]
values = [60, 100, 120]
print(knapsack(weights, values, 50))

#Longest Bitonic Subsequence
def bitonic(arr):
    n = len(arr)
    inc = [1] * n
    dec = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                inc[i] = max(inc[i], inc[j] + 1)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                dec[i] = max(dec[i], dec[j] + 1)
    return max(inc[i] + dec[i] - 1 for i in range(n))
print(bitonic([1, 11, 2, 10, 4, 5, 2, 1]))

#Minimum Deletions to Make a String Palindrome
def min_deletions(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i + 1][j],
                    dp[i][j - 1]
                )
    return n - dp[0][n - 1]
print(min_deletions("agbcba"))

#Dijkstra's Shortest Path
import heapq
def dijkstra(n, edges, source):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist
edges = [
    (0, 1, 2), (0, 2, 4),
    (1, 2, 1), (1, 3, 7),
    (2, 4, 3), (3, 4, 1)
]
print(dijkstra(5, edges, 0))

#Minimum Spanning Tree using Kruskal's Algorithm
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    parent = list(range(n))
    rank = [0] * n
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True
    total = 0
    count = 0
    for u, v, w in edges:
        if union(u, v):
            total += w
            count += 1
    return total if count == n - 1 else -1
edges = [
    (0, 1, 10), (0, 2, 6),
    (0, 3, 5), (1, 3, 15),
    (2, 3, 4)
]
print(kruskal(4, edges))

#Detect Negative Weight Cycle
def negative_cycle(n, edges):
    dist = [0] * n
    for i in range(n):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            return False
        if i == n - 1:
            return True
    return False
edges = [
    (0, 1, 1),
    (1, 2, -1),
    (2, 0, -1)
]
print(negative_cycle(3, edges))

#Topological Sorting of a DAG
from collections import deque
def topological_sort(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    if len(result) != n:
        return []
    return result
edges = [(0, 1), (0, 2), (1, 3)]
print(topological_sort(4, edges))

#Bridges in an Undirected Graph
def find_bridges(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = []
    def dfs(node, parent):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if tin[neighbor] != -1:
                low[node] = min(low[node], tin[neighbor])
            else:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > tin[node]:
                    bridges.append((node, neighbor))
    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
    return bridges
edges = [(0, 1), (1, 2), (2, 0), (1, 3)]
print(find_bridges(4, edges))

#Minimum Cost to Cut a Stick
def min_cost(n, cuts):
    cuts = [0] + sorted(cuts) + [n]
    m = len(cuts)
    dp = [[0] * m for _ in range(m)]
    for length in range(2, m):
        for i in range(m - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = (
                    cuts[j] - cuts[i]
                    + dp[i][k]
                    + dp[k][j]
                )
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][m - 1]
print(min_cost(7, [1, 3, 4, 5]))

#Egg Dropping Problem
def egg_drop(eggs, floors):
    dp = [0] * (eggs + 1)
    attempts = 0
    while dp[eggs] < floors:
        attempts += 1
        for e in range(eggs, 0, -1):
            dp[e] = dp[e] + dp[e - 1] + 1
    return attempts
print(egg_drop(2, 10))

#Maximum Rectangle of 1s in a Binary Matrix
def largest_histogram(heights):
    stack = []
    maximum = 0
    for i in range(len(heights) + 1):
        current = heights[i] if i < len(heights) else 0
        while stack and heights[stack[-1]] > current:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            maximum = max(maximum, h * width)
        stack.append(i)
    return maximum
def max_rectangle(matrix):
    if not matrix:
        return 0
    cols = len(matrix[0])
    heights = [0] * cols
    answer = 0
    for row in matrix:
        for j in range(cols):
            if row[j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
        answer = max(answer, largest_histogram(heights))
    return answer
matrix = [
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 1]
]
print(max_rectangle(matrix))

#Minimum Number of Refueling Stops
import heapq
def min_refuel(target, start_fuel, stations):
    fuel = start_fuel
    previous = 0
    stops = 0
    heap = []
    for position, amount in stations + [(target, 0)]:
        fuel -= position - previous
        while fuel < 0 and heap:
            fuel += -heapq.heappop(heap)
            stops += 1
        if fuel < 0:
            return -1
        heapq.heappush(heap, -amount)
        previous = position
    return stops
stations = [
    (10, 60), (20, 30),
    (30, 30), (60, 40)
]
print(min_refuel(100, 10, stations))

#Word Break – Minimum Number of Words
def min_words(s, dictionary):
    words = set(dictionary)
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] != float('inf') and s[j:i] in words:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n] if dp[n] != float('inf') else -1
s = "ilikeicecream"
dictionary = ["i", "like", "ice", "cream"]
print(min_words(s, dictionary))