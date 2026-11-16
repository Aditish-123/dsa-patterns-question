#Find a Pair with a Given Difference
def find_pair(arr, k):
    seen = set()
    for num in arr:
        if num - k in seen or num + k in seen:
            return True
        seen.add(num)
    return False
arr = [5, 20, 3, 2, 50, 80]
k = 78
print(find_pair(arr, k))

#Maximum Product of Three Numbers
def max_product(arr):
    arr.sort()
    n = len(arr)
    return max(
        arr[n-1] * arr[n-2] * arr[n-3],
        arr[0] * arr[1] * arr[n-1]
    )
arr = [10, 3, 5, 6, 20]
print(max_product(arr))

#String Compression
def compress(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    if s:
        result += s[-1] + str(count)
    return result
s = "aaabbcccc"
print(compress(s))