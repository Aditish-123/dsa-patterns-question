#Minimum Number of Refueling Stop
import heapq
def minRefuelStops(target, startFuel, stations):
    fuel = startFuel
    stops = 0
    i = 0
    heap = []
    while fuel < target:
        while i < len(stations) and stations[i][0] <= fuel:
            heapq.heappush(heap, -stations[i][1])
            i += 1
        if not heap:
            return -1
        fuel += -heapq.heappop(heap)
        stops += 1
    return stops
print(minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,30]]))

#Shortest Path in Binary Matrix
from collections import deque
def shortestPath(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    q = deque([(0, 0, 1)])
    visited = {(0, 0)}
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    while q:
        r, c, dist = q.popleft()
        if r == n-1 and c == n-1:
            return dist
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if (0 <= nr < n and 0 <= nc < n
                and grid[nr][nc] == 0
                and (nr, nc) not in visited):
                visited.add((nr, nc))
                q.append((nr, nc, dist+1))
    return -1
print(shortestPath([[0,1],[1,0]]))

#Find All Anagrams in a String
from collections import Counter
def findAnagrams(s, p):
    result = []
    k = len(p)
    if k > len(s):
        return result
    p_count = Counter(p)
    window = Counter(s[:k])
    if window == p_count:
        result.append(0)
    for i in range(k, len(s)):
        window[s[i]] += 1
        old = s[i-k]
        window[old] -= 1
        if window[old] == 0:
            del window[old]
        if window == p_count:
            result.append(i-k+1)
    return result
print(findAnagrams("cbaebabacd", "abc"))

#Maximum Sum Circular Subarray
def maxSubarraySumCircular(nums):
    total = sum(nums)
    max_sum = cur_max = nums[0]
    min_sum = cur_min = nums[0]
    for x in nums[1:]:
        cur_max = max(x, cur_max + x)
        max_sum = max(max_sum, cur_max)
        cur_min = min(x, cur_min + x)
        min_sum = min(min_sum, cur_min)
    if max_sum < 0:
        return max_sum
    return max(max_sum, total - min_sum)
print(maxSubarraySumCircular([5, -3, 5]))

#Remove K Digits
def removeKdigits(num, k):
    stack = []
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    result = ''.join(stack).lstrip('0')
    return result if result else "0"
print(removeKdigits("1432219", 3))

#Minimum Window Subsequence
def minWindow(s, t):
    n, m = len(s), len(t)
    best = ""
    i = 0
    while i < n:
        j = 0
        while i < n:
            if s[i] == t[j]:
                j += 1
            if j == m:
                break
            i += 1
        if j < m:
            break
        end = i
        j = m - 1
        while i >= 0:
            if s[i] == t[j]:
                j -= 1
            if j < 0:
                break
            i -= 1
        start = i
        if not best or end-start+1 < len(best):
            best = s[start:end+1]
        i = start + 1
    return best
print(minWindow("abcdebdde", "bde"))

#Maximum Number of Events That Can Be Attended
import heapq
def maxEvents(events):
    events.sort()
    heap = []
    i = 0
    day = 0
    count = 0
    n = len(events)
    while i < n or heap:
        if not heap:
            day = max(day, events[i][0])
        while i < n and events[i][0] <= day:
            heapq.heappush(heap, events[i][1])
            i += 1
        while heap and heap[0] < day:
            heapq.heappop(heap)
        if heap:
            heapq.heappop(heap)
            count += 1
            day += 1
    return count
print(maxEvents([[1,2],[2,3],[3,4]]))

#Find K-th Smallest Pair Distance
def smallestDistancePair(nums, k):
    nums.sort()
    def countPairs(distance):
        count = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > distance:
                left += 1
            count += right - left
        return count
    low = 0
    high = nums[-1] - nums[0]
    while low < high:
        mid = (low + high) // 2
        if countPairs(mid) >= k:
            high = mid
        else:
            low = mid + 1
    return low
print(smallestDistancePair([1,3,1], 1))

#Minimum Number of Taps to Open to Water a Garden
def minTaps(n, ranges):
    intervals = [0] * (n + 1)
    for i, r in enumerate(ranges):
        left = max(0, i-r)
        right = min(n, i+r)
        intervals[left] = max(intervals[left], right)
    taps = 0
    current_end = 0
    farthest = 0
    for i in range(n + 1):
        if i > farthest:
            return -1
        farthest = max(farthest, intervals[i])
        if i == current_end:
            if current_end == n:
                return taps
            taps += 1
            current_end = farthest
    return -1
print(minTaps(5, [3,4,1,1,0]))

#Path With Minimum Effort
import heapq
def minimumEffortPath(heights):
    rows = len(heights)
    cols = len(heights[0])
    effort = [[float('inf')] * cols for _ in range(rows)]
    effort[0][0] = 0
    heap = [(0, 0, 0)]
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    while heap:
        cost, r, c = heapq.heappop(heap)
        if r == rows-1 and c == cols-1:
            return cost
        if cost > effort[r][c]:
            continue
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = max(
                    cost,
                    abs(heights[r][c] - heights[nr][nc])
                )
                if new_cost < effort[nr][nc]:
                    effort[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
    return 0
print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))

#Count of Smaller Numbers After Self
def countSmaller(nums):
    arr = list(enumerate(nums))
    result = [0] * len(nums)
    def merge_sort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                result[left[i][0]] += j
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            result[left[i][0]] += j
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged
    merge_sort(arr)
    return result
print(countSmaller([5,2,6,1]))

#Maximum Frequency Stack
from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxfreq = 0
    def push(self, val):
        self.freq[val] += 1
        f = self.freq[val]
        self.maxfreq = max(self.maxfreq, f)
        self.group[f].append(val)
    def pop(self):
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val
fs = FreqStack()
fs.push(5)
fs.push(7)
fs.push(5)
fs.push(7)
fs.push(4)
fs.push(5)
print(fs.pop())
print(fs.pop())
print(fs.pop())

#Design Browser History
class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0
    def visit(self, url):
        self.history = self.history[:self.current+1]
        self.history.append(url)
        self.current += 1
    def back(self, steps):
        self.current = max(0, self.current-steps)
        return self.history[self.current]
    def forward(self, steps):
        self.current = min(
            len(self.history)-1,
            self.current+steps
        )
        return self.history[self.current]
browser = BrowserHistory("google.com")
browser.visit("youtube.com")
browser.visit("facebook.com")
print(browser.back(1))
print(browser.forward(1))

#Implement a Thread-Safe Task Queue
from queue import Queue
from threading import Thread
class TaskQueue:
    def __init__(self):
        self.tasks = Queue()
    def enqueue(self, task):
        self.tasks.put(task)
    def dequeue(self):
        return self.tasks.get()
    def task_done(self):
        self.tasks.task_done()
def worker(q):
    while True:
        task = q.dequeue()
        if task is None:
            q.task_done()
            break
        print("Processing:", task)
        q.task_done()
q = TaskQueue()
thread = Thread(target=worker, args=(q,))
thread.start()
q.enqueue("Task 1")
q.enqueue("Task 2")
q.enqueue("Task 3")
q.enqueue(None)
q.tasks.join()
thread.join()
