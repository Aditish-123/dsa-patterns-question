#Bubble Sort + Second Largest
arr = [12, 5, 8, 20, 3, 15]
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted list:", arr)
print("Second largest:", arr[-2])


#Merge Two Sorted Lists
a = [1, 4, 7, 10]
b = [2, 3, 6, 8, 9]
i = 0
j = 0
result = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1
result += a[i:]
result += b[j:]
print(result)
