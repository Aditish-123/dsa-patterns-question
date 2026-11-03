#Count Inversions in an Array
def count_inversions(arr):
    def merge_sort(a):
        if len(a) <= 1:
            return a, 0

        mid = len(a) // 2

        left, count1 = merge_sort(a[:mid])
        right, count2 = merge_sort(a[mid:])

        merged = []
        i = j = 0
        count = count1 + count2

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                count += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, count

    return merge_sort(arr)[1]


arr = [2, 4, 1, 3, 5]
print(count_inversions(arr))

#Maximum XOR of Two Numbers
def find_max_xor(nums):
    root = {}

    for num in nums:
        node = root

        for bit in range(31, -1, -1):
            b = (num >> bit) & 1
            node = node.setdefault(b, {})

    maximum = 0

    for num in nums:
        node = root
        current = 0

        for bit in range(31, -1, -1):
            b = (num >> bit) & 1
            opposite = 1 - b

            if opposite in node:
                current |= (1 << bit)
                node = node[opposite]
            else:
                node = node[b]

        maximum = max(maximum, current)

    return maximum


arr = [3, 10, 5, 25, 2, 8]
print(find_max_xor(arr))

#Smallest Range Covering Elements from K Lists
import heapq

def smallest_range(nums):
    heap = []
    maximum = float('-inf')

    for i in range(len(nums)):
        value = nums[i][0]
        heapq.heappush(heap, (value, i, 0))
        maximum = max(maximum, value)

    best_range = float('inf')
    answer = None

    while True:
        minimum, list_id, index = heapq.heappop(heap)

        if maximum - minimum < best_range:
            best_range = maximum - minimum
            answer = [minimum, maximum]

        if index + 1 == len(nums[list_id]):
            break

        next_value = nums[list_id][index + 1]

        heapq.heappush(
            heap,
            (next_value, list_id, index + 1)
        )

        maximum = max(maximum, next_value)

    return answer


lists = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]

print(smallest_range(lists))

#Maximum Sum Rectangle in a 2D Matrix
def max_sum_rectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    maximum = float('-inf')

    for left in range(cols):
        temp = [0] * rows

        for right in range(left, cols):

            for i in range(rows):
                temp[i] += matrix[i][right]

            current = temp[0]
            best = temp[0]

            for x in temp[1:]:
                current = max(x, current + x)
                best = max(best, current)

            maximum = max(maximum, best)

    return maximum


matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

print(max_sum_rectangle(matrix))

#Matrix Chain Multiplication
def matrix_chain(arr):
    n = len(arr)

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):

        for i in range(1, n - length + 1):
            j = i + length - 1

            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + arr[i - 1] * arr[k] * arr[j]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n - 1]


arr = [40, 20, 30, 10, 30]
print(matrix_chain(arr))

#Shortest Common Supersequence
def shortest_supersequence(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    lcs = dp[m][n]

    return m + n - lcs


print(shortest_supersequence("AGGTAB", "GXTXAYB"))

#Distinct Subsequences
def distinct_subsequences(s, t):
    m = len(s)
    n = len(t)

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, m + 1):

        for j in range(n, 0, -1):

            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]

    return dp[n]


print(distinct_subsequences("rabbbit", "rabbit"))

#Wildcard Pattern Matching
def wildcard_match(s, p):
    m = len(s)
    n = len(p)

    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if p[j - 1] == '*':
                dp[i][j] = (
                    dp[i][j - 1] or dp[i - 1][j]
                )

            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]


print(wildcard_match("adceb", "*a*b"))

#Boolean Parenthesization
def boolean_parenthesization(s):
    n = (len(s) + 1) // 2

    symbols = s[::2]
    operators = s[1::2]

    dp = [[(0, 0) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        if symbols[i] == 'T':
            dp[i][i] = (1, 0)
        else:
            dp[i][i] = (0, 1)

    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            true_count = 0
            false_count = 0

            for k in range(i, j):

                lt, lf = dp[i][k]
                rt, rf = dp[k + 1][j]

                op = operators[k]

                if op == '&':
                    true_count += lt * rt
                    false_count += lt * rf + lf * rt + lf * rf

                elif op == '|':
                    true_count += lt * rt + lt * rf + lf * rt
                    false_count += lf * rf

                elif op == '^':
                    true_count += lt * rf + lf * rt
                    false_count += lt * rt + lf * rf

            dp[i][j] = (true_count, false_count)

    return dp[0][n - 1][0]


print(boolean_parenthesization("T|F&F"))

#Strongly Connected Components
def strongly_connected(n, edges):
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = [False] * n
    order = []

    def dfs1(node):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)

        order.append(node)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    visited = [False] * n

    def dfs2(node):
        visited[node] = True

        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor)

    count = 0

    for node in reversed(order):
        if not visited[node]:
            dfs2(node)
            count += 1

    return count


edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (1, 3),
    (3, 4)
]

print(strongly_connected(5, edges))

#Floyd-Warshall Algorithm
def floyd_warshall(graph):
    n = len(graph)

    dist = [
        [float('inf') if x == -1 else x for x in row]
        for row in graph
    ]

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):

                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return [
        [-1 if x == float('inf') else x for x in row]
        for row in dist
    ]


graph = [
    [0, 5, -1, 10],
    [-1, 0, 3, -1],
    [-1, -1, 0, 1],
    [-1, -1, -1, 0]
]

for row in floyd_warshall(graph):
    print(*row)

#Minimum Edge Reversals to Reach Destination
from collections import deque

def min_reversals(n, edges, source, destination):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append((v, 0))
        graph[v].append((u, 1))

    dist = [float('inf')] * n
    dist[source] = 0

    dq = deque([source])

    while dq:
        node = dq.popleft()

        for neighbor, cost in graph[node]:
            new_dist = dist[node] + cost

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist

                if cost == 0:
                    dq.appendleft(neighbor)
                else:
                    dq.append(neighbor)

    return -1 if dist[destination] == float('inf') else dist[destination]


edges = [(0, 1), (2, 1), (2, 3)]

print(min_reversals(4, edges, 0, 3))

#Check Whether a Graph is Bipartite
from collections import deque

def is_bipartite(n, edges):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n

    for start in range(n):

        if color[start] != -1:
            continue

        q = deque([start])
        color[start] = 0

        while q:
            node = q.popleft()

            for neighbor in graph[node]:

                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    q.append(neighbor)

                elif color[neighbor] == color[node]:
                    return False

    return True


edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
]

print(is_bipartite(4, edges))

#Maximum Flow in a Network
from collections import deque

def maximum_flow(n, edges, source, sink):
    capacity = [[0] * n for _ in range(n)]

    for u, v, cap in edges:
        capacity[u][v] += cap

    total_flow = 0

    while True:
        parent = [-1] * n
        parent[source] = source

        q = deque([source])

        while q and parent[sink] == -1:
            u = q.popleft()

            for v in range(n):
                if capacity[u][v] > 0 and parent[v] == -1:
                    parent[v] = u
                    q.append(v)

        if parent[sink] == -1:
            break

        flow = float('inf')
        v = sink

        while v != source:
            u = parent[v]
            flow = min(flow, capacity[u][v])
            v = u

        v = sink

        while v != source:
            u = parent[v]

            capacity[u][v] -= flow
            capacity[v][u] += flow

            v = u

        total_flow += flow

    return total_flow


edges = [
    (0, 1, 16),
    (0, 2, 13),
    (1, 2, 10),
    (2, 1, 4),
    (1, 3, 12),
    (3, 2, 9),
    (2, 4, 14),
    (4, 3, 7),
    (3, 5, 20),
    (4, 5, 4)
]

print(maximum_flow(6, edges, 0, 5))

#Segment Tree – Range Sum Queries and Updates
class SegmentTree:

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):

        if start == end:
            self.tree[node] = arr[start]
            return

        mid = (start + end) // 2

        self.build(arr, 2 * node + 1, start, mid)
        self.build(arr, 2 * node + 2, mid + 1, end)

        self.tree[node] = (
            self.tree[2 * node + 1]
            + self.tree[2 * node + 2]
        )

    def update(self, index, value, node=0, start=0, end=None):

        if end is None:
            end = self.n - 1

        if start == end:
            self.tree[node] = value
            return

        mid = (start + end) // 2

        if index <= mid:
            self.update(index, value, 2 * node + 1, start, mid)
        else:
            self.update(index, value, 2 * node + 2, mid + 1, end)

        self.tree[node] = (
            self.tree[2 * node + 1]
            + self.tree[2 * node + 2]
        )

    def query(self, left, right, node=0, start=0, end=None):

        if end is None:
            end = self.n - 1

        if right < start or left > end:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        return (
            self.query(left, right, 2 * node + 1, start, mid)
            + self.query(left, right, 2 * node + 2, mid + 1, end)
        )


arr = [1, 3, 5, 7, 9, 11]

st = SegmentTree(arr)

print(st.query(1, 3))

st.update(1, 10)

print(st.query(1, 3))

#