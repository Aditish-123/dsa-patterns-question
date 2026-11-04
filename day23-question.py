#Subarrays with Exactly K Distinct Integers
def at_most_k(arr, k):
    if k < 0:
        return 0

    freq = {}
    left = 0
    count = 0

    for right in range(len(arr)):
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        while len(freq) > k:
            freq[arr[left]] -= 1

            if freq[arr[left]] == 0:
                del freq[arr[left]]

            left += 1

        count += right - left + 1

    return count


def exactly_k(arr, k):
    return at_most_k(arr, k) - at_most_k(arr, k - 1)


arr = [1, 2, 1, 2, 3]
print(exactly_k(arr, 2))
