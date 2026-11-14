#First Non-Repeating Character in a Live Stream
from collections import deque
def first_non_repeating(s):
    freq = {}
    q = deque()
    result = []
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)
        while q and freq[q[0]] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append(-1)
    return result
s = "aabc"
print(*first_non_repeating(s))

#One Edit Away
def one_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    i = 0
    j = 0
    edits = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            edits += 1
            if edits > 1:
                return False
            if len(s1) == len(s2):
                i += 1
                j += 1
            else:
                j += 1
    return True
print(one_edit_away("pale", "ple"))

#Maximum Subarray Sum with One Deletion
def max_sum_one_deletion(arr):
    keep = arr[0]
    delete = float('-inf')
    answer = arr[0]
    for num in arr[1:]:
        delete = max(keep, delete + num)
        keep = max(num, keep + num)
        answer = max(answer, keep, delete)
    return answer
arr = [1, -2, 0, 3]
print(max_sum_one_deletion(arr))

#Intersection of Two Linked Lists
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def intersection(headA, headB):
    a = headA
    b = headB
    while a is not b:
        if a is None:
            a = headB
        else:
            a = a.next
        if b is None:
            b = headA
        else:
            b = b.next
    return a
# Common linked list
shared = ListNode(8)
shared.next = ListNode(4)
shared.next.next = ListNode(5)
# List A
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = shared
# List B
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = shared
result = intersection(headA, headB)
if result:
    print(result.val)
else:
    print(-1)

#Compare Software Version Numbers
def compare_version(v1, v2):
    a = list(map(int, v1.split(".")))
    b = list(map(int, v2.split(".")))
    n = max(len(a), len(b))
    for i in range(n):
        x = a[i] if i < len(a) else 0
        y = b[i] if i < len(b) else 0
        if x > y:
            return 1
        elif x < y:
            return -1
    return 0
print(compare_version("1.0.12", "1.0.3"))

#Validate an IPv4 Address
def valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part:
            return False
        if not all(ch in "0123456789" for ch in part):
            return False
        if len(part) > 1 and part[0] == "0":
            return False
        if int(part) > 255:
            return False
    return True
print(valid_ip("192.168.1.01"))

#Minimum Swaps to Sort an Array
def min_swaps(arr):
    n = len(arr)
    arrpos = [(value, index) for index, value in enumerate(arr)]
    arrpos.sort()
    visited = [False] * n
    swaps = 0
    for i in range(n):
        if visited[i] or arrpos[i][1] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][1]
            cycle_size += 1
        swaps += cycle_size - 1
    return swaps
arr = [4, 3, 2, 1, 5]
print(min_swaps(arr))

#Shortest Path with One Discount Coupon
import heapq
def shortest_path(n, edges, src, dest):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    INF = float('inf')
    dist = [[INF, INF] for _ in range(n)]
    dist[src][0] = 0
    pq = [(0, src, 0)]
    while pq:
        cost, node, used = heapq.heappop(pq)
        if cost != dist[node][used]:
            continue
        for neighbour, weight in graph[node]:
            # Without using coupon
            new_cost = cost + weight
            if new_cost < dist[neighbour][used]:
                dist[neighbour][used] = new_cost
                heapq.heappush(
                    pq, (new_cost, neighbour, used)
                )
            # Using coupon
            if used == 0:
                new_cost = cost + weight // 2
                if new_cost < dist[neighbour][1]:
                    dist[neighbour][1] = new_cost
                    heapq.heappush(
                        pq, (new_cost, neighbour, 1)
                    )
    return min(dist[dest])
n = 4
edges = [
    (0, 1, 5),
    (0, 2, 10),
    (1, 2, 2),
    (1, 3, 9),
    (2, 3, 3)
]
print(shortest_path(n, edges, 0, 3))

#Minimum Deletions to Make Character Frequencies Unique
from collections import Counter
def min_deletions(s):
    freq = Counter(s)
    frequencies = sorted(
        freq.values(), reverse=True
    )
    used = set()
    deletions = 0
    for f in frequencies:
        while f > 0 and f in used:
            f -= 1
            deletions += 1
        if f > 0:
            used.add(f)
    return deletions
s = "aaabbbcc"
print(min_deletions(s))

#Minimum Cost Task Assignment
from functools import lru_cache
def min_assignment_cost(cost):
    n = len(cost)
    @lru_cache(None)
    def solve(mask):
        worker = mask.bit_count()
        if worker == n:
            return 0
        ans = float('inf')
        for task in range(n):
            if not (mask & (1 << task)):
                new_mask = mask | (1 << task)
                total = cost[worker][task] + solve(new_mask)
                ans = min(ans, total)
        return ans
    return solve(0)
cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]
print(min_assignment_cost(cost))
