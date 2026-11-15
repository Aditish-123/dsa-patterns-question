#Find the Leaders in an Array
def find_leaders(arr):
    leaders = []
    max_right = float('-inf')
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    return leaders[::-1]
arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))

#Find the Missing Ranges
def missing_ranges(arr, lower, upper):
    result = []
    prev = lower - 1
    for num in arr + [upper + 1]:
        if num - prev == 2:
            result.append(str(prev + 1))
        elif num - prev > 2:
            result.append(
                str(prev + 1) + "->" + str(num - 1)
            )
        prev = num
    return result
arr = [0, 1, 3, 50, 75]
print(missing_ranges(arr, 0, 99))

#Minimum Platforms Required
def minimum_platforms(arrival, departure):
    arrival.sort()
    departure.sort()
    i = 0
    j = 0
    platforms = 0
    max_platforms = 0
    while i < len(arrival):
        if arrival[i] <= departure[j]:
            platforms += 1
            i += 1
            max_platforms = max(
                max_platforms, platforms
            )
        else:
            platforms -= 1
            j += 1
    return max_platforms
arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print(minimum_platforms(arrival, departure))

#Check if Two Strings Are Rotations
def check_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = s1 + s1
    if s2 in temp:
        return True
    return False
s1 = "ABCD"
s2 = "CDAB"
print(check_rotation(s1, s2))

#Minimum Cost to Climb Stairs
def min_cost_climbing(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(
            dp[i - 1] + cost[i - 1],
            dp[i - 2] + cost[i - 2]
        )
    return dp[n]
cost = [10, 15, 20]
print(min_cost_climbing(cost))